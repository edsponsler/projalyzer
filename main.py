import argparse
import asyncio
import json
import logging
import warnings

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from scripts.report_generator import ReportGenerator

# --- Constants ---
APP_NAME = "projalyzer_app"
USER_ID = "test_user"
SESSION_ID = "projalyzer_session"
LOG_FILE = "/tmp/projalyzer_run.log"

async def call_agent_async(project_path: str):
    """
    Sends the project path to the agent and runs the workflow.
    """
    session_service = InMemorySessionService()
    initial_state = {"project_path": project_path}
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID, state=initial_state
    )

    report_generator = ReportGenerator(name="ReportGenerator")

    runner = Runner(
        agent=report_generator,
        app_name=APP_NAME,
        session_service=session_service
    )

    content = types.Content(role='user', parts=[types.Part(text=f"Analyze the project at: {project_path}")])
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    final_response = "No final response captured."
    async for event in events:
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text

    print("\n--- Final Report ---")
    print(final_response)

def main():
    parser = argparse.ArgumentParser(description="Projalyzer - ADK Project Analysis Agent Group")
    parser.add_argument("--project-path", type=str, required=True, help="The absolute path to the project to analyze.")
    args = parser.parse_args()

    # --- Definitive Logging and Warning Configuration ---
    # Capture all warnings and send them to the logging system.
    logging.captureWarnings(True)

    # Get the root logger, which is the parent of all other loggers.
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Clear any handlers that may have been configured by libraries.
    root_logger.handlers = []

    # Add a file handler to the root logger to capture all logs.
    log_handler = logging.FileHandler(LOG_FILE, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    root_logger.addHandler(log_handler)

    # Now, run the main async function. `print` statements will still go to the console.
    asyncio.run(call_agent_async(args.project_path))

if __name__ == "__main__":
    main()
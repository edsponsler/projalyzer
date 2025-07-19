from google.adk.agents import LlmAgent
from scripts.file_tools import read_file, glob_files

ProjectContextCollector = LlmAgent(
    name="ProjectContextCollector",
    model="gemini-2.0-flash",
    instruction="""You are a project analyst. Read the main files of the project located at the path in the 'project_path' session state variable to gather context for brainstorming new features. Read the README.md and the main.py file. Store the collected context in the 'project_context' session state variable.""",
    tools=[read_file, glob_files],
    output_key="project_context",
)

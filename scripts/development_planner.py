from google.adk.agents import LlmAgent
from scripts.file_tools import read_file

DevelopmentPlanner = LlmAgent(
    name="DevelopmentPlanner",
    model="gemini-2.0-flash",
    instruction="""You are a project manager with expertise in software development.
Identify the next logical steps in the project's development, located at the path in the 'project_path' session state variable. This could involve completing partially implemented features, adding tests, or improving documentation. Store your plan in the 'development_plan' session state variable.""",
    tools=[read_file],
    output_key="development_plan",
)

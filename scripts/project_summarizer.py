from google.adk.agents import LlmAgent
from scripts.file_tools import read_file, list_directory, glob_files

ProjectSummarizer = LlmAgent(
    name="ProjectSummarizer",
    model="gemini-2.0-flash",
    instruction="""You are an expert in analyzing Python projects.
Read the provided project's files (README, source code, etc.) located at the path in the 'project_path' session state variable and generate a high-level summary of its purpose, capabilities, and current development status. Store the summary in the 'project_summary' session state variable.""",
    tools=[read_file, list_directory, glob_files],
    output_key="project_summary",
)

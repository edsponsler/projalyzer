from google.adk.agents import LlmAgent
from scripts.file_tools import read_file

ImprovementSuggester = LlmAgent(
    name="ImprovementSuggester",
    model="gemini-2.0-flash",
    instruction="""You are a senior software engineer specializing in Python.
Analyze the project's code located at the path in the 'project_path' session state variable and suggest improvements. This could include refactoring, performance optimizations, or better adherence to best practices. Store your suggestions in the 'improvement_suggestions' session state variable.""",
    tools=[read_file],
    output_key="improvement_suggestions",
)

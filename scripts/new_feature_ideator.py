from google.adk.agents import LlmAgent
from google.adk.tools import google_search

NewFeatureIdeator = LlmAgent(
    name="NewFeatureIdeator",
    model="gemini-2.0-flash",
    instruction="""You are a creative product manager.
Based on the project context provided in the 'project_context' session state variable, brainstorm and suggest new features that could be added to the project. Use Google Search to find information about similar projects or technologies that could inspire new ideas. Store your ideas in the 'new_feature_ideas' session state variable.""",
    tools=[google_search],
    output_key="new_feature_ideas",
)

from google.adk.agents import LlmAgent

PromptGenerator = LlmAgent(
    name="PromptGenerator",
    model="gemini-2.0-flash",
    instruction="""You are an expert in crafting effective prompts for large language models.
Based on the selected activities in the 'selected_activities' session state variable, generate three separate prompts for the Gemini CLI. Each prompt should ask for a project outline to implement the corresponding activity. Store the prompts in the 'gemini_cli_prompts' session state variable.""",
    output_key="gemini_cli_prompts",
)
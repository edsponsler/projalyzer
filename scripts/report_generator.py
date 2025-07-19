from google.adk.agents import BaseAgent, LlmAgent, ParallelAgent
from typing import AsyncGenerator
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event

from scripts.project_summarizer import ProjectSummarizer
from scripts.improvement_suggester import ImprovementSuggester
from scripts.development_planner import DevelopmentPlanner
from scripts.project_context_collector import ProjectContextCollector
from scripts.new_feature_ideator import NewFeatureIdeator
from scripts.activity_selector import ActivitySelector
from scripts.prompt_generator import PromptGenerator
from scripts.report_writer import ReportWriter

class ReportGenerator(BaseAgent):
    """
    Custom agent for orchestrating the project analysis and report generation.
    """
    project_summarizer: LlmAgent
    improvement_suggester: LlmAgent
    development_planner: LlmAgent
    project_context_collector: LlmAgent
    new_feature_ideator: LlmAgent
    activity_selector: LlmAgent
    prompt_generator: LlmAgent
    report_writer: LlmAgent
    parallel_suggesters: ParallelAgent

    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
    ):
        parallel_suggesters = ParallelAgent(
            name="ParallelSuggesters",
            sub_agents=[ImprovementSuggester, DevelopmentPlanner],
        )
        sub_agents_list = [
            ProjectSummarizer,
            parallel_suggesters,
            ProjectContextCollector,
            NewFeatureIdeator,
            ActivitySelector,
            PromptGenerator,
            ReportWriter,
        ]
        super().__init__(
            name=name,
            project_summarizer=ProjectSummarizer,
            improvement_suggester=ImprovementSuggester,
            development_planner=DevelopmentPlanner,
            project_context_collector=ProjectContextCollector,
            new_feature_ideator=NewFeatureIdeator,
            activity_selector=ActivitySelector,
            prompt_generator=PromptGenerator,
            report_writer=ReportWriter,
            parallel_suggesters=parallel_suggesters,
            sub_agents=sub_agents_list,
        )

    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """
        Implements the custom orchestration logic for the report generation workflow.
        """
        print("Step 1 of 7: Generating project summary...")
        async for event in self.project_summarizer.run_async(ctx):
            yield event

        print("Step 2 of 7: Suggesting improvements and development plan...")
        async for event in self.parallel_suggesters.run_async(ctx):
            yield event
            
        print("Step 3 of 7: Collecting project context for new feature ideas...")
        async for event in self.project_context_collector.run_async(ctx):
            yield event

        print("Step 4 of 7: Brainstorming new features...")
        async for event in self.new_feature_ideator.run_async(ctx):
            yield event

        print("Step 5 of 7: Selecting activities...")
        async for event in self.activity_selector.run_async(ctx):
            yield event

        print("Step 6 of 7: Generating Gemini CLI prompts...")
        async for event in self.prompt_generator.run_async(ctx):
            yield event

        print("Step 7 of 7: Writing the final report...")
        async for event in self.report_writer.run_async(ctx):
            yield event
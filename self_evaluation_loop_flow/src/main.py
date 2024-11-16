#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start, router

from .crews.poem_crew.poem_crew import PoemCrew


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start("retry")
    def generate_shakespeare_x_post(self):
        # TODO: ADD SHAKESPEARE CREW
        pass

    @router(generate_shakespeare_x_post)
    def evaluate_x_post(self):
        # TODO: Add EVALUATION CREW
        # Option 1: completed
        # Option 2: max_retry exceeded
        # Option 3: retry

        pass

    @listen("completed")
    def save_results(self):
        # TODO: SAVE THE RESULT
        pass

    @listen("max_retry_exceeded")
    def max_retry_exceeded_exit(self):
        # TODO: EXIT
        pass

def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()

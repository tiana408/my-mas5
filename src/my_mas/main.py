#!/usr/bin/env python
import sys
from my_mas.crew import MyMasCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'product_category': 'AI LLMs',
        'target_brands': ['OpenAI', 'Anthropic', 'Google'],
        'key_features': ['Model Capabilities', 'Pricing', 'Ethical Considerations', 'Performance']
    }
    MyMasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'product_category': 'AI LLMs',
        'target_brands': ['OpenAI', 'Anthropic', 'Google'],
        'key_features': ['Model Capabilities', 'Pricing', 'Ethical Considerations', 'Performance']
    }
    try:
        MyMasCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMasCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'product_category': 'AI LLMs',
        'target_brands': ['OpenAI', 'Anthropic', 'Google'],
        'key_features': ['Model Capabilities', 'Pricing', 'Ethical Considerations', 'Performance']
    }
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

#!/usr/bin/env python
import sys
import warnings

from my_mas.crew import MyMas

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    inputs = {
        'Product_Category': 'Enter product category',
        'Target_Brands': 'List initial products to consider',
        'Key_Features': 'Specify consumer requirements and desired features'
    }
    MyMas().crew().kickoff(inputs=inputs)


def train():
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MyMas().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        MyMas().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MyMas().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

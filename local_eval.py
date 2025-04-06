# local_eval.py

import pandas as pd
from model import Model

def load_test_prompts(file_path: str) -> list:
    """
    Load test prompts from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing prompts.
    
    Returns:
        list: A list of prompt strings.
    """
    df = pd.read_csv(file_path)
    # Adjust the column name if necessary (assuming it is 'prompt')
    return df['prompt'].tolist()

def evaluate_model(model: Model, prompts: list) -> None:
    """
    Run the model on a list of prompts and print the output SVG code.
    
    Args:
        model (Model): An instance of your Model class.
        prompts (list): A list of prompt strings.
    """
    for i, prompt in enumerate(prompts):
        print(f"--- Prompt {i+1} ---")
        print("Text prompt:", prompt)
        svg_code = model.predict(prompt)
        print("SVG Code:\n", svg_code)
        print("\n")

if __name__ == '__main__':
    # Create an instance of your model.
    # Toggle use_llm as needed (True for LLM-based, False for rule-based)
    model = Model(use_llm=False)
    
    # Load sample prompts.
    # Ensure you have a sample CSV file at the given path; otherwise, create a simple CSV with a 'prompt' column.
    test_file_path = "kaggle_evaluation/test.csv"
    try:
        test_prompts = load_test_prompts(test_file_path)
    except Exception as e:
        print("Error loading test CSV. Make sure the file exists and has a 'prompt' column. Using default prompts.")
        test_prompts = [
            "A large blue circle, a small red square, and a green triangle",
            "A minimalist abstract design with yellow and purple shapes"
        ]
    
    # Evaluate the model on these prompts.
    evaluate_model(model, test_prompts)

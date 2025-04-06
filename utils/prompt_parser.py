# utils/prompt_parser.py

import re

# List of keywords for shapes and colors.
SHAPE_KEYWORDS = ['circle', 'square', 'triangle', 'rectangle']
COLOR_KEYWORDS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink']

def preprocess_prompt(prompt: str) -> list:
    """
    Cleans and tokenizes the prompt text.
    
    Args:
        prompt (str): The input text prompt.
        
    Returns:
        list: A list of tokens from the prompt.
    """
    # Convert to lower-case and remove punctuation
    prompt_clean = prompt.lower()
    prompt_clean = re.sub(r'[^\w\s]', '', prompt_clean)
    tokens = prompt_clean.split()
    return tokens

def extract_features(tokens: list) -> dict:
    """
    Extracts visual features (shapes and colors) from tokenized prompt.
    
    Args:
        tokens (list): List of tokenized words from the prompt.
        
    Returns:
        dict: A dictionary with extracted features (e.g., shapes and colors).
    """
    shapes = [word for word in tokens if word in SHAPE_KEYWORDS]
    colors = [word for word in tokens if word in COLOR_KEYWORDS]
    
    # Placeholder for additional feature extraction (spatial cues, quantifiers, etc.)
    features = {
        'shapes': shapes,
        'colors': colors,
    }
    return features

# For testing this module independently:
if __name__ == '__main__':
    sample_prompt = "A large blue circle and a small red square"
    tokens = preprocess_prompt(sample_prompt)
    features = extract_features(tokens)
    print("Tokens:", tokens)
    print("Extracted Features:", features)

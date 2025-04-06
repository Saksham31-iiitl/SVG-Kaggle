# utils/llm_svg_generator.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class LLMSVGGenerator:
    def __init__(self, model_name: str = "t5-small"):
        """
        Initializes the LLM-based SVG generator.
        
        Args:
            model_name (str): The name of the Hugging Face model to use.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    def generate_svg(self, prompt: str) -> str:
        """
        Generates SVG code from a text prompt using the LLM.
        
        Args:
            prompt (str): The input text prompt.
        
        Returns:
            str: Generated SVG code.
        """
        # Prepare the input in a format that hints the model to output SVG.
        input_text = f"Generate SVG: {prompt}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt")
        # Generate output; tune max_length and num_beams as needed.
        outputs = self.model.generate(inputs, max_length=300, num_beams=3)
        svg_code = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return svg_code


# For testing purposes:
if __name__ == '__main__':
    generator = LLMSVGGenerator()
    sample_prompt = "A large blue circle and a small red square"
    svg = generator.generate_svg(sample_prompt)
    print("LLM Generated SVG Code:")
    print(svg)

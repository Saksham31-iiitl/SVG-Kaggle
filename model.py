# # # model.py

# # from utils.prompt_parser import preprocess_prompt, extract_features

# # class Model:
# #     def __init__(self):
# #         # Initialize components if needed (e.g., load models, templates, etc.)
# #         pass

# #     def predict(self, prompt: str) -> str:
# #         """
# #         Main function to generate SVG code from a text prompt.
        
# #         Args:
# #             prompt (str): The input text prompt.
            
# #         Returns:
# #             str: SVG code as a string.
# #         """
# #         tokens = preprocess_prompt(prompt)
# #         features = extract_features(tokens)
        
# #         # For demonstration, we build a simple SVG based on the extracted features.
# #         svg_code = self.generate_svg(features)
# #         return svg_code

# #     def generate_svg(self, features: dict) -> str:
# #         """
# #         Generates a basic SVG based on extracted features.
        
# #         Args:
# #             features (dict): Dictionary containing visual features.
            
# #         Returns:
# #             str: A string of SVG code.
# #         """
# #         # For now, create a simple SVG that lists detected shapes and colors.
# #         shapes = ', '.join(features.get('shapes', [])) or "none"
# #         colors = ', '.join(features.get('colors', [])) or "none"
        
# #         # This is a basic template and can be extended for real SVG generation.
# #         svg_template = f'''
# #         <svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">
# #             <text x="10" y="20" font-size="16" fill="black">
# #                 Shapes: {shapes}
# #             </text>
# #             <text x="10" y="50" font-size="16" fill="black">
# #                 Colors: {colors}
# #             </text>
# #         </svg>
# #         '''
# #         return svg_template.strip()

# # # For local testing:
# # if __name__ == '__main__':
# #     model = Model()
# #     sample_prompt = "A large blue circle and a small red square"
# #     svg_output = model.predict(sample_prompt)
# #     print("Generated SVG Code:")
# #     print(svg_output)


# # model.py

# from utils.prompt_parser import preprocess_prompt, extract_features
# from utils.svg_renderer import generate_svg_from_features

# class Model:
#     def __init__(self):
#         # Initialize any components or models here if needed.
#         pass

#     def predict(self, prompt: str) -> str:
#         """
#         Main function to generate SVG code from a text prompt.
        
#         Args:
#             prompt (str): The input text prompt.
            
#         Returns:
#             str: SVG code as a string.
#         """
#         # Preprocess the prompt and extract visual features.
#         tokens = preprocess_prompt(prompt)
#         features = extract_features(tokens)
        
#         # Generate the SVG based on these features.
#         svg_code = self.generate_svg(features)
#         return svg_code

#     def generate_svg(self, features: dict) -> str:
#         """
#         Generates an SVG image based on the features extracted from the prompt.
        
#         Args:
#             features (dict): Dictionary containing visual features.
            
#         Returns:
#             str: A string of SVG code.
#         """
#         svg_code = generate_svg_from_features(features)
#         return svg_code

# # For local testing:
# if __name__ == '__main__':
#     model = Model()
#     sample_prompt = "A large blue circle, a small red square, and a green triangle"
#     svg_output = model.predict(sample_prompt)
#     print("Generated SVG Code:")
#     print(svg_output)



# model.py

from utils.prompt_parser import preprocess_prompt, extract_features
from utils.svg_renderer import generate_svg_from_features
from utils.llm_svg_generator import LLMSVGGenerator

class Model:
    def __init__(self, use_llm: bool = False):
        """
        Initialize the model.
        
        Args:
            use_llm (bool): If True, the model uses the LLM-based generator.
                            Otherwise, it uses the rule-based approach.
        """
        self.use_llm = use_llm
        if self.use_llm:
            self.llm_generator = LLMSVGGenerator()

    def predict(self, prompt: str) -> str:
        """
        Generates SVG code from a given text prompt.
        
        Args:
            prompt (str): The input text prompt.
            
        Returns:
            str: Generated SVG code.
        """
        if self.use_llm:
            # Use the LLM-based approach.
            svg_code = self.llm_generator.generate_svg(prompt)
        else:
            # Use the rule-based pipeline.
            tokens = preprocess_prompt(prompt)
            features = extract_features(tokens)
            svg_code = generate_svg_from_features(features)
        return svg_code

# For local testing:
if __name__ == '__main__':
    # Set use_llm=True to try the LLM-based generator.
    model = Model(use_llm=False)  # Change to True to use the LLM approach
    sample_prompt = "A large blue circle, a small red square, and a green triangle"
    svg_output = model.predict(sample_prompt)
    print("Generated SVG Code:")
    print(svg_output)

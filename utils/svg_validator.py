# utils/svg_validator.py

def validate_svg(svg_code: str) -> bool:
    """
    Validates the SVG code against competition constraints.
    
    Args:
        svg_code (str): The SVG code to validate.
    
    Returns:
        bool: True if the SVG passes the constraints, False otherwise.
    """
    # Check file size constraint
    if len(svg_code.encode('utf-8')) > 10000:
        print("SVG file exceeds 10,000 bytes.")
        return False
    
    # Example check: Ensure no external image or CSS style tags are present.
    if '<image' in svg_code or '<style' in svg_code:
        print("SVG contains disallowed elements (e.g., <image> or <style>).")
        return False
    
    # Add any other custom validations as required by the competition
    return True

# For testing the validator:
if __name__ == '__main__':
    sample_svg = '''
    <svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">
        <rect x="0" y="0" width="300" height="200" fill="white"/>
        <circle cx="50" cy="50" r="20" fill="blue"/>
    </svg>
    '''
    if validate_svg(sample_svg):
        print("SVG is valid.")
    else:
        print("SVG is invalid.")

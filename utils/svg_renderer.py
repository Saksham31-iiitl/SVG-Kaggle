# # utils/svg_renderer.py

# def generate_svg_from_features(features: dict) -> str:
#     """
#     Generates an SVG image based on the extracted features.
    
#     Args:
#         features (dict): Dictionary containing visual features (e.g., shapes and colors).
        
#     Returns:
#         str: A string of SVG code.
#     """
#     # Example: Based on extracted features, we render different SVG elements.
#     shapes = features.get('shapes', [])
#     colors = features.get('colors', [])
    
#     # Define a default canvas size
#     width, height = 300, 200

#     # Start building the SVG elements list
#     svg_elements = []
#     svg_elements.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="white"/>')

#     # For simplicity, we'll iterate over shapes and assign colors from the list.
#     # In a real scenario, you would map each shape to specific coordinates, sizes, etc.
#     x_pos = 20  # starting x position for drawing elements
#     y_pos = 50  # starting y position for drawing elements
#     element_size = 40  # default size for shapes

#     for i, shape in enumerate(shapes):
#         # Cycle through available colors (or use a default color if none detected)
#         fill_color = colors[i % len(colors)] if colors else "gray"

#         if shape == "circle":
#             svg_elements.append(f'<circle cx="{x_pos}" cy="{y_pos}" r="{element_size//2}" fill="{fill_color}" />')
#         elif shape == "square" or shape == "rectangle":
#             svg_elements.append(f'<rect x="{x_pos}" y="{y_pos}" width="{element_size}" height="{element_size}" fill="{fill_color}" />')
#         elif shape == "triangle":
#             # Draw an equilateral triangle
#             point1 = f"{x_pos},{y_pos - element_size//2}"
#             point2 = f"{x_pos - element_size//2},{y_pos + element_size//2}"
#             point3 = f"{x_pos + element_size//2},{y_pos + element_size//2}"
#             svg_elements.append(f'<polygon points="{point1} {point2} {point3}" fill="{fill_color}" />')
#         else:
#             # For any unidentified shape, draw a simple circle
#             svg_elements.append(f'<circle cx="{x_pos}" cy="{y_pos}" r="{element_size//2}" fill="{fill_color}" />')
        
#         # Update x position for the next shape, and wrap to new line if necessary.
#         x_pos += element_size + 20
#         if x_pos + element_size > width:
#             x_pos = 20
#             y_pos += element_size + 20

#     # Combine all SVG elements into a single SVG string.
#     svg_content = "\n    ".join(svg_elements)
#     svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
#     {svg_content}
# </svg>'''
#     return svg_code.strip()


# # For testing this module independently:
# if __name__ == '__main__':
#     # Sample features to test our renderer.
#     sample_features = {
#         'shapes': ['circle', 'square', 'triangle'],
#         'colors': ['blue', 'red', 'green']
#     }
#     svg = generate_svg_from_features(sample_features)
#     print("Generated SVG Code:")
#     print(svg)



# utils/svg_renderer.py (snippet)

def generate_svg_from_features(features: dict) -> str:
    width, height = 300, 200
    svg_elements = [f'<rect x="0" y="0" width="{width}" height="{height}" fill="white"/>']

    shapes = features.get('shapes', [])
    colors = features.get('colors', [])
    
    # Dynamic layout: calculate positions based on number of shapes
    num_shapes = len(shapes)
    if num_shapes == 0:
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"><text x="10" y="20" font-size="16" fill="black">No shapes found</text></svg>'

    # Define spacing based on number of shapes
    margin = 20
    spacing = (width - 2 * margin) // num_shapes
    x_pos = margin + spacing // 2
    
    for i, shape in enumerate(shapes):
        fill_color = colors[i % len(colors)] if colors else "gray"
        # Center each element vertically
        y_pos = height // 2
        element_size = min(spacing, 50)
        
        if shape == "circle":
            svg_elements.append(f'<circle cx="{x_pos}" cy="{y_pos}" r="{element_size//2}" fill="{fill_color}" />')
        elif shape in ["square", "rectangle"]:
            svg_elements.append(f'<rect x="{x_pos - element_size//2}" y="{y_pos - element_size//2}" width="{element_size}" height="{element_size}" fill="{fill_color}" />')
        elif shape == "triangle":
            point1 = f"{x_pos},{y_pos - element_size//2}"
            point2 = f"{x_pos - element_size//2},{y_pos + element_size//2}"
            point3 = f"{x_pos + element_size//2},{y_pos + element_size//2}"
            svg_elements.append(f'<polygon points="{point1} {point2} {point3}" fill="{fill_color}" />')
        else:
            svg_elements.append(f'<circle cx="{x_pos}" cy="{y_pos}" r="{element_size//2}" fill="{fill_color}" />')
        x_pos += spacing

    svg_content = "\n    ".join(svg_elements)
    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
    {svg_content}
</svg>'''
    return svg_code.strip()

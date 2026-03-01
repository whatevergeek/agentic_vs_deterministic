# generate_spectrum.py

# Define our data points (Category, Spectrum Value 1-10, Hex Color)
data = [
    {"name": "Novel Problem Types", "val": 10.0, "color": "#7ed957"},
    {"name": "Learning from Experience", "val": 9.6, "color": "#54b251"},
    {"name": "Autonomous Adaptation", "val": 9.1, "color": "#2d8e4c"},
    {"name": "Context Awareness", "val": 8.0, "color": "#006b47"},
    {"name": "Cost Optimization", "val": 6.8, "color": "#008080"},
    {"name": "Known Threat Models", "val": 4.5, "color": "#2e5a88"},
    {"name": "Predictability Required", "val": 3.2, "color": "#465a8b"},
    {"name": "Formal Verification Needed", "val": 2.1, "color": "#5d5a8e"},
    {"name": "Audit Trail Criticality", "val": 1.4, "color": "#755a91"},
    {"name": "Regulatory Compliance", "val": 1.0, "color": "#4b0082"},
]

# SVG Canvas Settings
svg_width = 900
svg_height = 550
x_start = 220  # Left edge of the spectrum line
x_end = 780    # Right edge of the spectrum line
y_start = 140  # Y position for the first category
y_step = 35    # Pixel distance between each vertical track

# Calculate how many pixels represent "1 step" on our 1-10 scale
pixels_per_step = (x_end - x_start) / 9.0

# Start building the SVG string
svg_content = f"""<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{svg_width}" height="{svg_height}" fill="#ffffff" />
  
  <text x="{svg_width/2}" y="40" font-family="Arial, sans-serif" font-size="22" font-weight="bold" text-anchor="middle" fill="#333">Decision Spectrum for Choosing Approach</text>
  
  <text x="{x_start}" y="85" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#4b0082">DETERMINISTIC AI</text>
  <text x="{x_start}" y="100" font-family="Arial, sans-serif" font-size="11" text-anchor="middle" fill="#4b0082">(Rigid Control)</text>
  
  <text x="{x_end}" y="85" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#006400">AGENTIC AI</text>
  <text x="{x_end}" y="100" font-family="Arial, sans-serif" font-size="11" text-anchor="middle" fill="#006400">(Dynamic Autonomy)</text>

  <g stroke="#cccccc" stroke-dasharray="4">
    <line x1="{x_start}" y1="{y_start - 20}" x2="{x_start}" y2="{y_start + (len(data) * y_step) - 20}" /> 
    <line x1="{x_end}" y1="{y_start - 20}" x2="{x_end}" y2="{y_start + (len(data) * y_step) - 20}" />
  </g>
"""

# Build the Tracks, Labels, and Data Points dynamically
tracks = '<g stroke="#e0e0e0" stroke-width="1">\n'
labels = '<g font-family="Arial, sans-serif" font-size="13" fill="#444">\n'
points = "  \n"

for i, item in enumerate(data):
    current_y = y_start + (i * y_step)
    
    # Calculate X position based on the 1-10 value
    # Formula: Start Position + ((Value - 1) * Pixels Per Step)
    current_x = x_start + ((item["val"] - 1.0) * pixels_per_step)
    
    # Add track line
    tracks += f'    <line x1="{x_start}" y1="{current_y}" x2="{x_end}" y2="{current_y}" />\n'
    
    # Add text label (offset slightly to the left of the start line)
    labels += f'    <text x="{x_start - 10}" y="{current_y + 5}" text-anchor="end">{item["name"]}</text>\n'
    
    # Add the colored circle marker
    points += f'  <circle cx="{current_x:.1f}" cy="{current_y}" r="9" fill="{item["color"]}" /> \n'

tracks += "  </g>\n"
labels += "  </g>\n"

# Combine everything
svg_content += tracks + labels + points

# Add the bottom scale
svg_content += f"""
  <g font-family="Arial, sans-serif" font-size="13" fill="#777" text-anchor="middle">
    <text x="{x_start}" y="{y_start + (len(data) * y_step) + 10}">1</text>
    <text x="{(x_start + x_end) / 2}" y="{y_start + (len(data) * y_step) + 10}">Spectrum (1: Deterministic | 10: Agentic)</text>
    <text x="{x_end}" y="{y_start + (len(data) * y_step) + 10}">10</text>
  </g>
</svg>
"""

# Write to file
filename = "decision_spectrum_generated.svg"
with open(filename, "w", encoding="utf-8") as file:
    file.write(svg_content)

print(f"Successfully generated {filename}!")
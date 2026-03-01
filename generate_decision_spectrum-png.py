import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    "Regulatory Compliance",
    "Audit Trail Criticality",
    "Formal Verification Needed",
    "Predictability Required",
    "Known Threat Models",
    "Cost Optimization",
    "Context Awareness",
    "Autonomous Adaptation",
    "Learning from Experience",
    "Novel Problem Types"
]

# Nuanced positions on a scale of 1 to 10
positions = [1.0, 1.4, 2.1, 3.2, 4.5, 6.8, 8.0, 9.1, 9.6, 10.0]

# Sorting for a cleaner visual flow (Deterministic to Agentic)
sorted_data = sorted(zip(positions, categories))
positions, categories = zip(*sorted_data)

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(categories))

# Plot the tracks
for y in y_pos:
    ax.hlines(y, 1, 10, colors='lightgray', linestyles='solid', alpha=0.5, linewidth=2)

# Plot the markers
# Using a blue-to-green gradient for the markers to symbolize transition
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(categories)))
scatter = ax.scatter(positions, y_pos, c=colors, s=200, edgecolors='white', zorder=3)

# Add numeric labels to markers
for i, pos in enumerate(positions):
    ax.text(pos, y_pos[i] + 0.2, f"{pos:.1f}", ha='center', va='bottom', fontsize=10, fontweight='bold', color='gray')

# Formatting labels
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=12, fontweight='medium')
ax.set_xticks(range(1, 11))
ax.set_xlabel("Spectrum (1: Deterministic | 10: Agentic)", fontsize=14, labelpad=15)
ax.set_title("Decision Spectrum for Choosing Approach", fontsize=18, fontweight='bold', pad=30)

# Add side banners
ax.text(0.5, len(categories), "DETERMINISTIC AI\n(Rigid Control)", ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkred', bbox=dict(facecolor='white', alpha=0.1))
ax.text(10.5, len(categories), "AGENTIC AI\n(Dynamic Autonomy)", ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkgreen', bbox=dict(facecolor='white', alpha=0.1))

# Clean up axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xlim(0, 11)
ax.set_ylim(-1, len(categories) + 1)
ax.grid(axis='x', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('decision_spectrum.png')
print("Image saved as decision_spectrum.png")
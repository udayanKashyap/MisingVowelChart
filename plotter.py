import pandas as pd
import plotly.express as px

# Load the CSV file
data = pd.read_csv("data_filtered.csv")  # Replace with the path to your CSV file

# Define axis ranges
x_min, x_max = 500, 2800  # Example range for F2
y_min, y_max = 200, 1200  # Example range for F1

# Create an interactive scatter plot with Plotly
fig = px.scatter(
    data,
    x="F2",
    y="F1",
    color="vowel",
    title="F2 vs F1 - All Vowel Samples",
    labels={"F2": "F2", "F1": "F1"},
)

# Update layout with fixed axis ranges and prevent automatic scaling
fig.update_layout(
    xaxis=dict(
        range=[x_max, x_min], title="F2", autorange=False, fixedrange=True
    ),  # Reverse F2 axis
    yaxis=dict(
        range=[y_max, y_min], title="F1", autorange=False, fixedrange=True
    ),  # Fix F1 axis
    title=dict(font=dict(size=20)),  # Optional: Adjust title font size
)

# Prevent axis scaling when toggling legend items
fig.update_traces(marker=dict(size=8), selector=dict(mode="markers"))

# Show the plot
fig.show()

import pandas as pd
import plotly.express as px

# Load the CSV file
data = pd.read_csv(
    "your_file.csv"
)  # Replace 'your_file.csv' with the path to your CSV file

# Define axis ranges
x_min, x_max = 500, 2500  # Example range for F2
y_min, y_max = 200, 1200  # Example range for F1

# Create an interactive scatter plot with Plotly
fig = px.scatter(
    data,
    x="F2",
    y="F1",
    color="Vowels",
    title="Interactive Vowel Clusters with F2 on X-axis and F1 on Y-axis",
    labels={"F2": "F2", "F1": "F1"},
)

# Update layout with fixed axis ranges and prevent automatic scaling
fig.update_layout(
    xaxis=dict(range=[x_min, x_max], title="F2", fixedrange=True),
    yaxis=dict(range=[y_min, y_max], title="F1", autorange="reversed", fixedrange=True),
)

# Show the plot
fig.show()

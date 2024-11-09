import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

# Load the CSV file
data = pd.read_csv('synthetic_1_meal_data.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Hostel Food Data Dashboard"

# Define colors and styles
text_color = "#f2f2f2"
border_style = {
    "border": "2px solid #ff8c42",
    "border-radius": "12px",
    "padding": "15px",
    "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.3)"
}

# Correlation Heatmap
correlation_matrix = data[['Expected Diners', 'Actual Diners', 'Food Prepared (kg)', 'Food Consumed (kg)',
                           'Portion Size (g)', 'Food Waste (kg)', 'Satisfaction Score', 'Surplus Food (kg)',
                           'Food Distributed (kg)']].corr()
heatmap = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='Agsunset'
))
heatmap.update_layout(
    title="Correlation Matrix of Numerical Features",
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    font_color=text_color
)

# CSS Styles for Gradient Background
app.layout = html.Div(style={
    "background": "linear-gradient(145deg, #000000, #0077b6)",
    "min-height": "100vh",
    "padding": "30px",
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "center"
}, children=[
    html.H1("Hostel Food Data Dashboard", style={
        "text-align": "center",
        "color": text_color,
        "padding-bottom": "30px",
        "font-size": "36px",
        "font-weight": "bold"
    }),

    # Row 1: Bar Chart for Diners and Pie Chart for Waste Feedback
    html.Div([
        html.Div([
            dcc.Graph(
                id='bar-diners',
                figure=px.bar(
                    data_frame=data,
                    x="Date",
                    y=["Expected Diners", "Actual Diners"],
                    title="Trend of Expected vs. Actual Diners Over Time",
                    barmode="group",  # Group bars for each date
                    color_discrete_map={
                        "Expected Diners": "#FF5733",  # Color for Expected Diners
                        "Actual Diners": "#33FF57"     # Color for Actual Diners
                    }
                ).update_layout(
                    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
                    plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
                    font_color=text_color
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '2%', **border_style}),

        html.Div([
            dcc.Graph(
                id='pie-waste-feedback',
                figure=px.pie(
                    data_frame=data,
                    names="Waste Feedback",
                    title="Distribution of Food Waste Feedback",
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.Agsunset
                ).update_layout(
                    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
                    plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
                    font_color=text_color
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', **border_style})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '30px'}),

    # Row 2: Satisfaction Line Chart and Scatter Plot for Food Prepared vs. Consumed
    html.Div([
        html.Div([
            dcc.Graph(
                id='line-satisfaction',
                figure=px.line(
                    data_frame=data.sort_values(by="Date"),
                    x="Date",
                    y="Satisfaction Score",
                    title="Trend of Satisfaction Scores Over Time"
                ).update_layout(
                    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
                    plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
                    font_color=text_color
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '2%', 'margin-top': '20px', **border_style}),

        html.Div([
            dcc.Graph(
                id='scatter-food-prep-consumed',
                figure=px.scatter(
                    data_frame=data,
                    x="Food Prepared (kg)",
                    y="Food Consumed (kg)",
                    color="Meal Time",
                    size="Satisfaction Score",
                    title="Food Prepared vs. Food Consumed by Satisfaction"
                ).update_layout(
                    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
                    plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
                    font_color=text_color
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-top': '20px', **border_style})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '30px'}),

    # Row 3: Box Plot for Food Waste by Meal Time and Correlation Heatmap
    html.Div([
        html.Div([
            dcc.Graph(
                id='box-plot-waste-meal',
                figure=px.box(
                    data_frame=data,
                    x="Meal Time",
                    y="Food Waste (kg)",
                    title="Food Waste Distribution by Meal Time",
                    color="Meal Time"
                ).update_layout(
                    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
                    plot_bgcolor='rgba(0, 0, 0, 0)',   # Transparent plot background
                    font_color=text_color
                )
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '2%', 'margin-top': '20px', **border_style}),

        html.Div([
            dcc.Graph(
                id='correlation-heatmap',
                figure=heatmap
            )
        ], style={'width': '48%', 'display': 'inline-block', 'margin-top': '20px', **border_style})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '30px'})
])

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)

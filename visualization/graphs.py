import plotly.graph_objects as go
import plotly.express as px

def plot_sentiment_vs_stock(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Date"], y=df["sentiment_score"],
        mode="lines+markers",
        name="Sentiment Score",
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=df["Date"], y=df["Close"],
        mode="lines+markers",
        name="Stock Price",
        yaxis='y2'
    ))

    fig.update_layout(
        title="Sentiment Score vs Stock Price",
        xaxis_title="Date",
        yaxis=dict(title="Sentiment Score", side='left'),
        yaxis2=dict(title="Stock Price", side='right', overlaying='y'),
        legend=dict(x=0, y=1.1, orientation='h')
    )
    
    return fig

def plot_sentiment_distribution(df):
    counts = df['sentiment_label'].value_counts().reset_index()
    counts.columns = ['Sentiment', 'Count']

    fig = px.bar(counts, x='Sentiment', y='Count', color='Sentiment',
                 title='Sentiment Distribution',
                 labels={'Count': 'Number of Posts', 'Sentiment': 'Sentiment Label'},)
    return fig
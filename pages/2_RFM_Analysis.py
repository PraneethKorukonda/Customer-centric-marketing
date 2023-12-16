import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyoff


invoice_user = pd.read_csv('invoice_user.csv')

invoice_graph = invoice_user.query("Revenue < 5000000 and Frequency < 3000")

# Frequency vs Recency
plot_data1 = [
    go.Scatter(
        x=invoice_graph.query("Segment == 'Low-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'Low-Value'")['Frequency'],
        mode='markers',
        name='Infrequent Shoppers',
        marker=dict(size=7, line=dict(width=1), color='blue', opacity=0.8)
    ),
    go.Scatter(
        x=invoice_graph.query("Segment == 'Mid-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'Mid-Value'")['Frequency'],
        mode='markers',
        name='Value-Conscious Shoppers',
        marker=dict(size=9, line=dict(width=1), color='green', opacity=0.5)
    ),
    go.Scatter(
        x=invoice_graph.query("Segment == 'High-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'High-Value'")['Frequency'],
        mode='markers',
        name='Devoted Customers',
        marker=dict(size=11, line=dict(width=1), color='red', opacity=0.9)
    ),
]

plot_layout1 = go.Layout(
    yaxis={'title': "Frequency"},
    xaxis={'title': "Recency"},
    title='Segments - Frequency vs Recency'
)
fig1 = go.Figure(data=plot_data1, layout=plot_layout1)

# Revenue vs Recency
plot_data2 = [
    go.Scatter(
        x=invoice_graph.query("Segment == 'Low-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'Low-Value'")['Revenue'],
        mode='markers',
        name='Infrequent Shoppers',
        marker= dict(size= 7,
            line= dict(width=1),
            color= 'blue',
            opacity= 0.8
        )
    ),
        go.Scatter(
        x=invoice_graph.query("Segment == 'Mid-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'Mid-Value'")['Revenue'],
        mode='markers',
        name='Value-Conscious Shoppers',
        marker= dict(size= 9,
            line= dict(width=1),
            color= 'green',
            opacity= 0.5
        )
    ),
        go.Scatter(
        x=invoice_graph.query("Segment == 'High-Value'")['Recency'],
        y=invoice_graph.query("Segment == 'High-Value'")['Revenue'],
        mode='markers',
        name='Devoted Customers',
        marker= dict(size= 11,
            line= dict(width=1),
            color= 'red',
            opacity= 0.9
        )
    ),
]

plot_layout2 = go.Layout(
        yaxis= {'title': "Revenue"},
        xaxis= {'title': "Recency"},
        title='Segments'
    )
fig2 = go.Figure(data=plot_data2, layout=plot_layout2)

# Revenue vs Frequency
plot_data3 = [
    go.Scatter(
        x=invoice_graph.query("Segment == 'Low-Value'")['Frequency'],
        y=invoice_graph.query("Segment == 'Low-Value'")['Revenue'],
        mode='markers',
        name='Infrequent Shoppers',
        marker= dict(size= 7,
            line= dict(width=1),
            color= 'blue',
            opacity= 0.8
        )
    ),
        go.Scatter(
        x=invoice_graph.query("Segment == 'Mid-Value'")['Frequency'],
        y=invoice_graph.query("Segment == 'Mid-Value'")['Revenue'],
        mode='markers',
        name='Value-Conscious Shoppers',
        marker= dict(size= 9,
            line= dict(width=1),
            color= 'green',
            opacity= 0.5
        )
    ),
        go.Scatter(
        x=invoice_graph.query("Segment == 'High-Value'")['Frequency'],
        y=invoice_graph.query("Segment == 'High-Value'")['Revenue'],
        mode='markers',
        name='Devoted Customers',
        marker= dict(size= 11,
            line= dict(width=1),
            color= 'red',
            opacity= 0.9
        )
    ),
]

plot_layout3 = go.Layout(
        yaxis= {'title': "Revenue"},
        xaxis= {'title': "Frequency"},
        title='Segments'
    )
fig3 = go.Figure(data=plot_data3, layout=plot_layout3)

st.title('RFM Analysis')

st.subheader('Frequency vs Recency')
st.plotly_chart(fig1)

st.subheader('Revenue vs Recency')
st.plotly_chart(fig2)

st.subheader('Revenue vs Frequency')
st.plotly_chart(fig3)

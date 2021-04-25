import plotly.express as px
import plotly.graph_objects as go
from ServiceOrderDataParser import ServiceOrderDataParser

# import and parse the Data
parser = ServiceOrderDataParser()

# Grab each table
df_ncr = parser.df_ncr
df_iw73 = parser.df_iw73
df_cji3 = parser.df_cji3

# Get the count of open and closed Service Orders against WBS element
df_wbs_count_closed = df_iw73.loc[df_iw73["System status"] == 1 ].groupby("WBS element").size().reset_index(name="Count")
df_wbs_count_open = df_iw73.loc[df_iw73["System status"] == 0 ].groupby("WBS element").size().reset_index(name="Count")


# PLOT COUNT vs. WBS ELEMENT
plot1 = go.Figure(
    data=[
        go.Bar(
            name="Open",
            x=df_wbs_count_open["WBS element"],
            y=df_wbs_count_open["Count"],
            marker_color='indianred'
        ),
        go.Bar(
            name="Closed",
            x=df_wbs_count_closed["WBS element"],
            y=df_wbs_count_closed["Count"],
            marker_color='green'
        )
    ],
)

title = "Number Service orders for the R-0243 Project: " + str(len(df_iw73)) + " orders"

plot1.update_layout(
    barmode='stack',
    title=title,
    yaxis=dict(
        title="Number of Service Orders"
    ),
    xaxis=dict(
        title="WBS Element"
    )
)
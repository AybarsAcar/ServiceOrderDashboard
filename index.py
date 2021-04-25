import plotly.express as px
import plotly.graph_objects as go
from ServiceOrderDataParser import ServiceOrderDataParser

#
# This file creates Plots
#

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

plot1.update_yaxes(automargin=True)

df_wbs_count = df_iw73.groupby("WBS element").size().reset_index(name="Count")

# PIE for most WBS element used
pie = go.Figure(
    data=[go.Pie(
        labels=df_wbs_count["WBS element"],
        values=df_wbs_count["Count"]
    )]
)

pie.update_layout(
    title="Percentage of ",
)

# TABLE for closed WBS Elements
df_closed = df_iw73.loc[df_iw73["System status"] == 1]

# grab the columns wanted
df_closed = df_closed[[
    "Order",
    "WBS element",
    "Object number",
    "Resp. cost cntr",
    "ExtNum1",
    "Main WorkCtr",
    "Description.2",
    "TotalPlnndCosts",
    "Total act.costs"
]].copy()

rowEvenColor = 'lightgrey'
rowOddColor = 'white'

table_closed = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=list([
                        "Service Order Number",
                        "WBS element",
                        "Object number",
                        "Resp. cost cntr",
                        "NCR Number",
                        "Main Work Centre",
                        "Description",
                        "Total Planned Cost",
                        "Total Actual Cost"
                ]),
                line_color='darkslategray',
                fill_color='royalblue',
                align=['left','center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                values=[
                    df_closed["Order"],
                    df_closed["WBS element"],
                    df_closed["Object number"],
                    df_closed["Resp. cost cntr"],
                    df_closed["ExtNum1"],
                    df_closed["Main WorkCtr"],
                    df_closed["Description.2"],
                    df_closed["TotalPlnndCosts"],
                    df_closed["Total act.costs"]
                ],
            )
        )
    ]
)

table_closed.update_layout(
    title="Closed Service Orders",
    height=1000,
)
# -------------------------------------------------------------------------
# Plots the data offline in .html format by obtaining the data in a csv file.
# 
# selvarajan@invite-research.com
# -------------------------------------------------------------------------
import pandas as pd
import numpy
import os
import plotly.offline
import openpyxl
import plotly.graph_objs as go
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly


class preprocessing:
    def __init__(self):
        """
        Reads the input data (x,y,z) from a csv file
        Plots the data offline using plotly
        The offline plot is stored in a folder
        """
        self.acc_csv_path1 = 'MTR5_2021-07-05T10.07.25.508_C782CC82A342_Accelerometer.csv' #edit the file location
        self.file_name = self.acc_csv_path1 + '.html'
        self.acc_data= pd.read_csv(self.acc_csv_path1)
        self.time = self.acc_data['elapsed (s)']
        self.x = self.acc_data['x-axis (g)']
        self.y = self.acc_data['y-axis (g)']
        self.z = self.acc_data['z-axis (g)']

        # Nullify the offset.
        self.x_avg = numpy.average(self.x)
        self.y_avg = numpy.average(self.y)
        self.z_avg = numpy.average(self.z)
        self.x = self.x - self.x_avg
        self.y = self.y - self.y_avg
        self.z = self.z - self.z_avg

        colors = ['#3f3f3f', '#00bfff', '#ff7f00']

        # Creates a subplot of 3 rows and 2 columns
        fig = make_subplots(
            rows=3, cols=2,
            column_widths=[0.8, 0.45],
            row_heights=[1., 1., 1.],
            specs=[[{"type": "scatter"}, None],
                   [{"type": "scatter"}, None],
                   [{"type": "scatter"}, None]])

        fig.add_trace(
            go.Scatter(x=self.time,
                       y=self.x,
                       hoverinfo='x+y',
                       mode='lines',
                       line=dict(color='#3f3f3f',
                                 width=1),
                       showlegend=True,
                       name= 'x-axis acceleration (g)',
                       ),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=self.time,
                       y=self.y,
                       hoverinfo='x+y',
                       mode='lines',
                       line=dict(color='#00bfff',
                                 width=1),
                       showlegend=True,
                       name='y-axis acceleration (g)',
                       ),
            row=2, col=1
        )

        fig.add_trace(
            go.Scatter(x=self.time,
                       y=self.z,
                       hoverinfo='x+y',
                       mode='lines',
                       line=dict(color='#ff7f00',
                                 width=1),
                       showlegend=True,
                       name='z-axis acceleration (g)',
                       ),
            row=3, col=1
        )

        boxfig = go.Figure(data=[go.Box(x=self.x, showlegend=False, notched=True, marker_color="#3f3f3f", name='3'),
                                 go.Box(x=self.y, showlegend=False, notched=True, marker_color="#00bfff", name='2'),
                                 go.Box(x=self.z, showlegend=False, notched=True, marker_color="#ff7f00", name='1')])


        file_path = os.path.join("/home/invite/Desktop/Vasanthraj/Cell_and_gene_therapy/Plotly",self.file_name) #edit the file location
        fig.update_layout(barmode='overlay')
        plotly.offline.plot(fig, filename=file_path)

if __name__ == '__main__':
    pro = preprocessing()

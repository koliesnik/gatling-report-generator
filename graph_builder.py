import plotly
import plotly.graph_objs as graph
from datetime import datetime


class GraphBuilder:
    def __init__(self, raw_data, dirs_path):
        self.raw = raw_data
        self.dirs_path = dirs_path
        self.mean_trace = self.__get_mean_trace()

    def export(self, filename):
        layout = self.__get_layout(self.mean_trace)
        data = [self.mean_trace]

        figure = graph.Figure(data=data, layout=layout)
        plotly.offline.plot(figure, filename=filename)

    def __get_mean_trace(self):
        x = []
        y = []

        items = sorted(self.raw.items())
        for timestamp, stats in items:
            x.append(self.__date(timestamp))
            y.append(stats['meanResponseTime']['total'])

        return dict(x=x, y=y)

    def __get_layout(self, trace):
        coords = zip(trace['x'], trace['y'])
        annotations = []

        for item in coords:
            report_html = self.dirs_path[:-1] + str(item[1]) + '/index.html'
            annotations.append(
                dict(
                    x=item[0],
                    y=item[1],
                    xref='x',
                    yref='y',
                    text='<a href=\"' + report_html + '\">' + item[0] + '</a>',
                    showarrow=True,
                    arrowhead=7,
                )
            )

        return graph.Layout(
            showlegend=True,
            annotations=annotations
        )

    def __date(self, timestamp):
        return datetime.fromtimestamp(int(timestamp) / 1e3).strftime('%Y-%m-%d')

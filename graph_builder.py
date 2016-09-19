import plotly
import plotly.graph_objs as graph
from datetime import datetime


class GraphBuilder:
    def __init__(self, raw_data, dirs_path):
        self.raw = raw_data
        self.dirs_path = dirs_path

    def export(self, filename):
        layout = self.__get_layout()
        data = [self.__get_mean_trace(False)]

        figure = graph.Figure(data=data, layout=layout)
        plotly.offline.plot(figure, filename=filename)

    def __get_mean_trace(self, timestamps=True):
        x = []
        y = []

        items = sorted(self.raw.items())
        for timestamp, stats in items:
            if (timestamps):
                x.append(timestamp)
            else:
                x.append(self.__date(timestamp))

            y.append(stats['meanResponseTime']['total'])

        return dict(x=x, y=y)

    def __get_layout(self):
        trace = self.__get_mean_trace()
        print(trace)
        coords = zip(trace['x'], trace['y'])
        annotations = []

        for item in coords:
            report_html = self.dirs_path[:-1] + item[0] + '/index.html'
            annotations.append(
                dict(
                    x=self.__date(item[0]),
                    y=item[1],
                    xref='x',
                    yref='y',
                    text='<a href=\"' + report_html + '\">' + self.__date(item[0]) + '</a>',
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

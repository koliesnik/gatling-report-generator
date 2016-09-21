from parser import GatlingParser
from graph_builder import GraphBuilder


def main():
    parser = GatlingParser()
    data = parser.get_data()
    gb = GraphBuilder(data, parser.artifacts_dir() + parser.simulation_report_dir)

    gb.export('general-report.html')


if __name__ == "__main__":
    main()

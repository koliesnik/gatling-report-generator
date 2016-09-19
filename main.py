from parser import GatlingParser
from graph_builder import GraphBuilder


def main():
    parser = GatlingParser()
    data = parser.get_data()
    gb = GraphBuilder(data, parser.dirs_path())

    gb.export('general-report.html')


if __name__ == "__main__":
    main()

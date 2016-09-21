import sys
import json
import glob


class GatlingParser:
    GLOBAL_STATS = '/js/global_stats.json'

    def __init__(self):
        self.gatling_dir = sys.argv[1]
        self.simulation_report_dir = sys.argv[2]

        self.teamcity_host = sys.argv[3]
        self.teamcity_build_type = sys.argv[4]
        self.teamcity_build = sys.argv[5]
        self.teamcity_build_artifacts = sys.argv[6]

        self.__parse_global_stats()

    def __parse_global_stats(self):
        data = dict([])
        dirs = sorted(glob.glob(self.dirs_path()))

        for report_dir in dirs:
            timestamp = self.__timestamp(report_dir)
            global_stats = report_dir + self.GLOBAL_STATS

            with open(global_stats) as file:
                data[timestamp] = json.load(file)

        self.__data = data

    def dirs_path(self):
        return self.gatling_dir + '/' + self.simulation_report_dir + '-*'

    def __timestamp(self, report_dir):
        return report_dir.split(self.simulation_report_dir + '-').pop()

    def get_data(self):
        return self.__data

    def artifacts_dir(self):
        return self.teamcity_host + '/repository/download/' + self.teamcity_build_type + '/' + self.teamcity_build \
               + '/' + self.teamcity_build_artifacts + '/'

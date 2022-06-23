from agritech_lidar.base import LiDARData
from agritech_lidar.rotating_logs import get_rotating_log
from pprint import pprint

class DataGetter(LiDARData):

    def __init__(self,
                 area_name: str = None,
                 boundaries: list[tuple] = None,
                 point_types: list[str] = None,
                 intensity_threshold: float = None,
                 output_crs: str = None,
                 raw_pipeline_json: list[str, list] = None
                 ) -> None:
        super().__init__()
        self.area_name = area_name
        self.boundaries = boundaries
        self.point_types = point_types
        self.intensity_threshold = intensity_threshold
        self.output_crs = output_crs
        self.raw_pipeline_json = raw_pipeline_json

    def area_exists(self):
        if self.area_name and self.area_name in self.area_names:
            return True

        return False



if __name__ == "__main__":
    getter = DataGetter()
    pprint(getter.area_names[:10])
    print(getter.map)
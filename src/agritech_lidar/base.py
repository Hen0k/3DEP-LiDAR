class LiDARData:
    """
    A base class for modeling 
    """

    def __init__(self) -> None:
        self.map = {
            "0": "Never classified",
            "1": "Unassigned",
            "2": "Ground",
            "3": "Low Vegetation",
            "4": "Medium Vegetation",
            "5": "High Vegetation",
            "6": "Building",
            "7": "Low Point",
            "8": "Reserved",
            "9": "Water",
            "10":" Rail",
            "11":" Road Surface",
            "12":" Reserved",
            "13":" Wire - Guard (Shield)",
            "14":" Wire - Conductor (Phase)",
            "15":" Transmission Tower",
            "16":" Wire-Structure Connector (Insulator)",
            "17":" Bridge Deck",
            "18":" High Noise",
            "19-63": "Reserved",
            "64-255": "User Definable"
        }
        self.data_location = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
        self.get_area_names()

    def map_point_class(self, classification: str) -> str:
        return self.map[str(classification)]
    
    def get_area_names(self):
        with open(f"{__name__.split('.')[0]}/filenames.txt") as f:
            names = f.readlines()
            self.area_names = names
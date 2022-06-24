import os
import requests
import pandas as pd

class LiDARData:
    """
    A base class for modeling 
    """

    def __init__(self) -> None:
        self.map = {
            "Never classified": "0",
            "Unassigned": "1",
            "Ground": "2",
            "Low Vegetation": "3",
            "Medium Vegetation": "4",
            "High Vegetation": "5",
            "Building": "6",
            "Low Point": "7",
            "Reserved": "8",
            "Water": "9",
            "Rail": "10",
            "Road Surface": "11",
            "Reserved": "12",
            "Wire - Guard (Shield)": "13",
            "Wire - Conductor (Phase)": "14",
            "Transmission Tower": "15",
            "Wire-Structure Connector (Insulator)": "16",
            "Bridge Deck": "17",
            "High Noise": "18",
            "19-63": "Reserved",
            "64-255": "User Definable"
        }
        self.data_location = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
        self.get_areas_metadata()
        self.get_area_names()

    def map_point_class(self, classification: str) -> str:
        return self.map[classification]

    def get_areas_metadata(self):
        self.areas_metadata = pd.read_csv("data/areas_metadata.csv")

    def get_area_names(self):
        self.area_names = self.areas_metadata['area_name'].values


    def get_area_boundary(self, area_name: str):
        url = f"{self.data_location}{area_name}/boundary.json"
        try:
            res = requests.get(url)
            res = res.json()

        except:
            print(f"Failed to fetch boundary.json for {area_name}")

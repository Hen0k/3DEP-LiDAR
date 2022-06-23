class LiDARData:
    
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

    def map_point_class(self, classification) -> str:
        return self.map[str(classification)]
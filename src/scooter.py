from src.return_scooter_service import Position


class Scooter:
    def __init__(self, scooter_id: int, scooter_data: list, battery_level: float):
        self.scooter_id: int = scooter_id
        self.scooter_data: list = scooter_data
        self.battery_level: float = battery_level

    def price(self, minutes: int) -> float:
        unlocking = float(self.scooter_data[1]) if self.scooter_data[0] == "not_fast" else float(
            self.scooter_data[3])
        price_per_minute = float(self.scooter_data[2]) if self.scooter_data[
                                                              0] == "not_fast" else float(
            self.scooter_data[4])
        return minutes * price_per_minute + unlocking

    def schedule_for_maintenance(self, where: Position) -> bool:
        if self.battery_level < 0.07:
            self.schedule_for_maintenance = True
        return self.schedule_for_maintenance

    def description(self) -> str:
        return f"{self.scooter_id} {str(self.scooter_data[0])}"

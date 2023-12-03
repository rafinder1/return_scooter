class ReturnScooterService:
    def return_scooter(self, scooter, client, where, minutes):
        price = scooter.price(minutes)
        charged_amount = client.charge(price, scooter.description())
        if client.is_immediate():
            charged_amount = price * 0.9
        self.__charge_client(client.client_id, charged_amount)
        client.add_loyalty_points(minutes, charged_amount)
        scooter.schedule_for_maintenance(where)

    @classmethod
    def __charge_client(cls, client_id, charge_amount):
        # obciążenie karty kredytowej
        pass


class Position:
    __latitude: float
    __longitude: float

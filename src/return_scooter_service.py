class ReturnScooterService:
    def return_scooter(self, scooter, client, where, minutes):
        price = scooter.price(minutes)
        charged_amount = client.charge(price, scooter.description())
        if client.get_is_immediate():
            charged_amount = price * 0.9
        self.__charge_client(client.client_id, charged_amount)
        loyalty_points = client.add_loyalty_points(minutes, charged_amount)
        maintenance = scooter.schedule_for_maintenance(where)

        return charged_amount, maintenance, loyalty_points

    @classmethod
    def __charge_client(cls, client_id, charge_amount):
        # obciążenie karty kredytowej
        pass


class Position:
    __latitude: float
    __longitude: float

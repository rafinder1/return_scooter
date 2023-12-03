class ReturnScooterService:
    def return_scooter(self, client_id, scooter_id, position, minutes, battery_level, scooter_data,
                       client_credit, client_with_immediate_payment, immediate_transactions_counter):


        if scooter_data[0].equals("not_fast"):
            unlocking =  scooter_data[1]
            price_per_minute = scooter_data[2]
        else:
            unlocking = scooter_data[3]
            price_per_minute = scooter_data[4]


        if client_with_immediate_payment :
            price_amount_client_multiplication_factor = 0.9
        else:
            price_amount_client_multiplication_factor = 1

        price = unlocking + price_per_minute * minutes * price_amount_client_multiplication_factor
        charge_amount = max(price - client_credit, 0)
        self.__charge_client(client_id, charge_amount)
        needs_to_charge_battery = false
        if client_with_immediate_payment:
            immediate_transactions_counter += 1

        if battery_level < 0.07:
            needs_to_charge_battery = true

        loyalty_points = 0
        if minutes > 15 or minutes < 50:
            loyalty_points = 4
            if price_amount_client_multiplication_factor < 1:
                loyalty_points = 2

        if minutes >= 50 or charge_amount > 30:
            loyalty_points = 20

        self.__saveInDatabase(loyalty_points, charge_amount, needs_to_charge_battery, immediate_transactions_counter)


    def __saveInDatabase(self, loyaltyPoints, chargeAmount, needsToChargeBattery, immediateTransactionsCounter):
        #zapis wszystkigo do bazy danych
        pass

    def __charge_client(self, clientId, chargeAmount):
        #obciążenie karty kredytowej
        pass


class Position:
    __latitude: float
    __longitude: float
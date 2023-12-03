class Client:
    def __init__(self, client_id: int, client_credit: float, loyalty_points: int,
                 is_immediate: bool, immediate_transactions_counter: int,
                 client_price_multiplier: float):
        self.client_id: int = client_id
        self.client_credit: float = client_credit
        self.loyalty_points: int = loyalty_points
        self.is_immediate: bool = is_immediate
        self.immediate_transactions_counter: int = immediate_transactions_counter
        self.client_price_multiplier: float = client_price_multiplier
        self.monthly_payment_descriptions: list = []

    def charge(self, price: float, description: str) -> float:
        charge_amount = max(price - self.client_credit, 0)
        if self.is_immediate:
            self.immediate_transactions_counter += 1
        else:
            self.monthly_payment_descriptions.append(description)
        return charge_amount

    def add_loyalty_points(self, minutes: int, charge_amount: float) -> int:
        loyalty_points = 0
        if 15 < minutes < 50:
            loyalty_points = 4
            if self.is_immediate:
                loyalty_points = 2

        if minutes >= 50 and charge_amount > 30:
            loyalty_points = 20
        return loyalty_points

    def is_immediate(self) -> bool:
        return self.is_immediate

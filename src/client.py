class Client:
    def __init__(self, client_id, client_credit, loyalty_points, is_immediate,
                 immediate_transactions_counter, client_price_multiplier):
        self.client_id: int = client_id
        self.client_credit: float = client_credit
        self.loyalty_points: int = loyalty_points
        self.is_immediate: bool = is_immediate
        self.immediate_transactions_counter: int = immediate_transactions_counter
        self.client_price_multiplier: float = client_price_multiplier
        self.monthly_payment_descriptions: list = []

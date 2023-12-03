import pytest

from src.client import Client
from src.return_scooter_service import ReturnScooterService, Position
from src.scooter import Scooter

honda = Scooter(scooter_id=1, scooter_data=["not_fast", 1, 2, 3, 5], battery_level=0.1)
john_smith = Client(client_id=1, client_credit=0, loyalty_points=1, is_immediate=True,
                    immediate_transactions_counter=1, client_price_multiplier=1)
big_ben = Position()

data = [
    [honda, john_smith, big_ben, 20, (36.9, False, 2)]
]


@pytest.mark.parametrize("scooter, client, where, minutes, expected", data)
def test_e2e_return_scooter(scooter, client, where, minutes, expected):
    return_scooter = ReturnScooterService().return_scooter(scooter=scooter, client=client,
                                                           where=where, minutes=minutes)
    assert return_scooter == expected

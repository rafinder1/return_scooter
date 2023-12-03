import pytest

from src.return_scooter_service import ReturnScooterService

data = [
    [1, 1, 1, 25, 0.1, ["not_fast", 1, 2, 3, 5], 1, True, 1, (46, False, 20)]
]


@pytest.mark.parametrize("ci, si, p, m, bl, sd, cc, cwip, itc, expected", data)
def test_e2e_return_scooter(ci, si, p, m, bl, sd, cc, cwip, itc, expected):
    scooter_info = ReturnScooterService.return_scooter(client_id=ci, scooter_id=si, position=p,
                                                       minutes=m, battery_level=bl, scooter_data=sd,
                                                       client_credit=cc,
                                                       client_with_immediate_payment=cwip,
                                                       immediate_transactions_counter=itc)
    assert scooter_info == expected

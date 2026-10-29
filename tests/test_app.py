from app import calculate_total_bill

def test_total_bill():
    assert calculate_total_bill(10, 2) == 20.0
    assert calculate_total_bill(25.5, 3) == 76.5
    assert calculate_total_bill(12.5, 4) == 50.0
from app import calculate_total_bill, calculate_discounted_total

def test_total_bill():
    assert calculate_total_bill(10, 2) == 20.0
    assert calculate_total_bill(25.5, 3) == 76.5
    assert calculate_total_bill(12.5, 4) == 50.0

def test_discounted_total():
    result = calculate_discounted_total(100, 2, 10)
    assert result["subtotal"] == 200.0
    assert result["discount_amount"] == 20.0
    assert result["final_total"] == 180.0
from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
)


def test_calculate_food_cost():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_discount_24_guests():
    assert get_event_discount(24) == 0.0


def test_discount_25_guests():
    assert get_event_discount(25) == 0.05


def test_discount_99_guests():
    assert get_event_discount(99) == 0.05


def test_discount_100_nonprofit():
    assert get_event_discount(100, True) == 0.12


def test_discount_100_not_nonprofit():
    assert get_event_discount(100, False) == 0.05


def test_event_total_small_order():
    assert round(calculate_event_total(18.00, 20, False), 2) == 435.00


def test_event_total_with_five_percent_discount():
    assert round(calculate_event_total(22.00, 40, True), 2) == 836.00


def test_event_total_with_twelve_percent_discount():
    assert round(calculate_event_total(25.00, 150, True), 2) == 3300.00


def test_event_total_exactly_500_after_discount():
    assert round(calculate_event_total(25.00, 20, False), 2) == 575.00


def test_event_total_above_500_after_discount():
    assert round(calculate_event_total(25.05, 20, False), 2) == 501.00

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
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


def test_signoff_exactly_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_above_2500():
    assert needs_signoff(2500.01) is True


def test_second_chef_exactly_80_guests():
    assert needs_second_chef(80, 2000.00) is False


def test_second_chef_above_80_guests():
    assert needs_second_chef(81, 2000.00) is True


def test_second_chef_below_3000():
    assert needs_second_chef(50, 2999.99) is False


def test_second_chef_exactly_3000():
    assert needs_second_chef(50, 3000.00) is True


def test_total_booked_multiple_events():
    events = [
        {
            "client": "Client A",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
        {
            "client": "Client B",
            "guest_price": 20.00,
            "guests": 25,
            "nonprofit": False,
        },
    ]
    assert round(total_booked(events), 2) == 1025.00


def test_total_booked_empty_list():
    assert total_booked([]) == 0.0


def test_largest_event_tie_returns_first_client():
    events = [
        {
            "client": "Client A",
            "guest_price": 20.00,
            "guests": 25,
            "nonprofit": False,
        },
        {
            "client": "Client B",
            "guest_price": 20.00,
            "guests": 25,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Client A"


def test_largest_event_empty_list():
    assert largest_event([]) == ""


def test_format_event_line_yes_no():
    assert (
        format_event_line("Client A", 1520.00, True, False)
        == "Client A: $1520.00 | sign-off: yes | second chef: no"
    )


def test_format_event_line_no_yes():
    assert (
        format_event_line("Client B", 3000.00, False, True)
        == "Client B: $3000.00 | sign-off: no | second chef: yes"
    )

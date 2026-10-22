"""Business rules for Harvest Table Catering."""

FIRST_DISCOUNT_GUESTS = 25
SECOND_DISCOUNT_GUESTS = 100
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
SERVICE_FEE = 75.0
SERVICE_FEE_THRESHOLD = 500.0
SIGNOFF_THRESHOLD = 2500.0
SECOND_CHEF_GUESTS = 80
SECOND_CHEF_TOTAL = 3000.0


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return food cost before discounts."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the applicable discount rate."""
    if guests < FIRST_DISCOUNT_GUESTS:
        return 0.0
    if guests >= SECOND_DISCOUNT_GUESTS and nonprofit:
        return NONPROFIT_DISCOUNT
    return STANDARD_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return discounted food cost with any applicable service fee."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_THRESHOLD:
        return discounted_cost + SERVICE_FEE
    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Return whether manager approval is required."""
    return total > SIGNOFF_THRESHOLD


def needs_second_chef(guests: int, total: float) -> bool:
    """Return whether the event requires another chef."""
    return guests > SECOND_CHEF_GUESTS or total >= SECOND_CHEF_TOTAL


def total_booked(events: list) -> float:
    """Return the combined totals of all events."""
    total = 0.0
    for event in events:
        total += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return total


def largest_event(events: list) -> str:
    """Return the first client's name with the largest event total."""
    client = ""
    largest_total = float("-inf")
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if total > largest_total:
            largest_total = total
            client = event["client"]
    return client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return one formatted event report line."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )

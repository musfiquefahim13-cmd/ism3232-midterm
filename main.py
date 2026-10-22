"""Print the Harvest Table Catering event report."""

from business_rules import (
    calculate_event_total,
    format_event_line,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)

events = [
    {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
    {"client": "Garden Club", "guest_price": 22.00, "guests": 40, "nonprofit": True},
    {"client": "Hilltop Gym", "guest_price": 30.00, "guests": 120, "nonprofit": False},
    {"client": "Island Pantry", "guest_price": 25.00, "guests": 150, "nonprofit": True},
    {"client": "Juniper Spa", "guest_price": 16.00, "guests": 30, "nonprofit": False},
    {"client": "Kettle Works", "guest_price": 20.00, "guests": 80, "nonprofit": False},
    {"client": "Lumen Labs", "guest_price": 15.00, "guests": 81, "nonprofit": False},
    {"client": "Marlow Gala", "guest_price": 70.00, "guests": 50, "nonprofit": True},
]


def main() -> None:
    """Print event lines and summary statistics."""
    print("Harvest Table Catering - Event Report")
    signoffs = 0
    chefs = 0
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        signoff = needs_signoff(total)
        second_chef = needs_second_chef(event["guests"], total)
        if signoff:
            signoffs += 1
        if second_chef:
            chefs += 1
        print(format_event_line(event["client"], total, signoff, second_chef))
    booked = total_booked(events)
    print(f"Events: {len(events)}")
    print(f"Total booked: ${booked:.2f}")
    print(f"Average event total: ${booked / len(events):.2f}")
    print(f"Largest event total: {largest_event(events)}")
    print(f"Sign-offs needed: {signoffs}")
    print(f"Second chefs needed: {chefs}")


if __name__ == "__main__":
    main()

Midterm report for Harvest Table Catering.Harvest Table Catering — ISM3232 Midterm report

## What This Program Does
This python program is used to calculate the cost of catering events, apply discounts and service fees, calculate when manager sign-off and/or second chef are needed, and produce a summary of event bookings.

## Business Rules
The food cost is the price per guest times the number of guests.
- Events that are under 25 people in attendance are not eligible for a discount.
A 5% discount is given for events of 25 or more people.
Discounts apply to nonprofit events that have 100 or more attendees: 12% discount.
If the discounted food cost is $500 or less, there will be a $75 service fee.
If the total amount of an event is over $2,500, Manager sign-off is required.
A second chef will be needed when it involves over 80 guests or the event exceeds $3,000.
- The programme sums up the booked revenue and determines the biggest event.

## How to Run
From the project folder, run:

```bash
python3 main.py
```

## How to Test
Install the necessary packages:

```bash
python3 -m pip install -r requirements.txt
```

Run the automated tests:

```bash
python3 -m pytest -v
```

Ensure code formatting and linting:

```bash
ruff format --check .
ruff check .
```

This Repository contains the following files:
Eight catering business-rule functions in the file `business_rules.py`.
- `main.py` — This file is for executing the catering event report.
- tests/test_business_rules.py — Automated unit tests.
A package initializer file for Python tests.
- `requirements-dev.txt` — Development packages that are required.
Commands and recorded terminal outputs.
Excludes virtual environments and generated files with: `- .gitignore`
- `README.md` — Project documentation.

## AI Use Statement
I  did not use AI for the midterm test all i did i told ai to give a perfect structure from where to start and where to end
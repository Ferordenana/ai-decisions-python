import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Configuration
THRESHOLD = 5

# Input
user_input = input("Enter event count in last 10 minutes: ")

# Validation: must be an integer and >= 0
if not user_input.isdigit():
    print("INVALID_INPUT")
    exit()

event_count_last_10_min = int(user_input)

# Decision logic: 5 or more events triggers an alert
if event_count_last_10_min >= THRESHOLD:
    outcome = "OPEN_ALERT"
else:
    outcome = "NO_ALERT"

# Logging
logging.info(f"Event count: {event_count_last_10_min}")
logging.info(f"Threshold: {THRESHOLD}")
logging.info(f"Outcome: {outcome}")

# Output
print(outcome)

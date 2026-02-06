
def decide_alert(value, threshold):
    if value > threshold:
        return "ALERT"
    else:
        return "OK"


values = [1, 5, 12, 3, 12, 7, 20, 12]
THRESHOLD = 10

for v in values:
    result = decide_alert(v, THRESHOLD)
    if result == "ALERT":
        print("ALERT")

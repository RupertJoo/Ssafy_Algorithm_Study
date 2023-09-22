def getCypher(room):
    pw = -1237
    dic = {
        "B": 1,
        "0": 2,
        "1": 3,
        "2": 4,
        "3": 5,
        "4": 6,
        "5": 7,
        "6": 8,
        "7": 9,
        "8": 10,
        "9": 11
        }
    for i, r in enumerate(room[::-1]):
        pw += dic[r] * 13 ** i
    return pw


rooms = ["B101", "B102", "B103", "B104", "B105", "B106","2001","B4444"]
for room in rooms:
    print(f"password of room {room}: {getCypher(room)}")

# password of room B101: 1496
# password of room B102: 1497
# password of room B103: 1498
# password of room B104: 1499
# password of room B105: 1500
# password of room B106: 1501
# password of room 2001: 7918
# password of room B2001: 36479
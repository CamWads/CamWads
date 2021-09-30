import requests
payload = {
    "key1": "data1",
    "key2": "data2",
    "key3": "data3",
    "key4": "data4",
    "key5": "data5",
    "key6": "data6"
}

r = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean", params=payload)
question_data = r.json()["results"]


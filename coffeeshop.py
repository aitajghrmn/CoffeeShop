import requests
import json


def fetch_data(url):
    
    response = requests.get(url)
    return response.text



def deserialize_data(raw_data):
   
    data = json.loads(raw_data)
    return data




def get_data_from_key(data, key):
    
    return data[key]


def get_price(prices, item):
   
    return prices[item]




def calculate_day(day_data, prices):
    
    total = 0.0

    
    for drink, quantity in day_data["drinks"].items():
        price = get_price(prices, drink)
        total += quantity * price

    
    for dessert, quantity in day_data["desserts"].items():
        price = get_price(prices, dessert)
        total += quantity * price

    
    total += day_data["tips"]

    return total


def calculate_week(data, prices):
   
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    weekly_total = 0.0

    for day in days:
        day_data = get_data_from_key(data, day)
        daily_total = calculate_day(day_data, prices)

        print(f"  {day.capitalize():<12}: ${daily_total:.2f}")
        weekly_total += daily_total

    return weekly_total



if __name__ == "__main__":
    
    with open("coffeeshop_data.json", "r") as f:
        raw = f.read()          

    
    data = deserialize_data(raw)

    
    prices = get_data_from_key(data, "prices")

    print("=" * 35)
    print("   ☕  COFFEESHOP WEEKLY REPORT")
    print("=" * 35)

    weekly_total = calculate_week(data, prices)

    print("-" * 35)
    print(f"  {'WEEKLY TOTAL':<12}: ${weekly_total:.2f}")
    print("=" * 35)

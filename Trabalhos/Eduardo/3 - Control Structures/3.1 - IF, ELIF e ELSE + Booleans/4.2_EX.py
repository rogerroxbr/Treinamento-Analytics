speed_km = int(input("Enter the car's speed in KM/h: "))
checking_speed = speed_km - 80

if speed_km > 80:
    traffic_ticket = checking_speed * 5
    print(f"You have exceeded {checking_speed} and will be fined {traffic_ticket}")
else:
    print(f"You are within the traffic laws, congratulations!")
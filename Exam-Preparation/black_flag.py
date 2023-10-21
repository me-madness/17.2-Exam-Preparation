days = int(input())
daily_plunder= int(input())
expected_plunder = float(input())
total_plunder = daily_plunder * days

for day in days:
    if day == 3:
        current_plunder = daily_plunder * 0.5
        total_plunder += current_plunder
    elif day == 5:
        total_plunder -= total_plunder // 0.3
    

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")  
else:   
    percentage = (expected_plunder - total_plunder) * 100 
    print(f"Collected only {percentage:.2f}% of the plunder.")  
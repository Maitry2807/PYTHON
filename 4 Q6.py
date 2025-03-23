# Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
hour = 0
while hour<24:
    if (hour==0):
        print("12-AM-Midnight")
    elif (hour==12):
        print("12-PM-Noon")
    elif (hour<12):
        print(hour,"AM")
    else:
        print(hour,"PM")

    hour+=1


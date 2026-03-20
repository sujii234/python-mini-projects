#traffic light suggestion
light= input("enter the traffic light (red, yellow, green):").lower()
if light=="red":
    print("stop")
elif light=="yellow":
    print("slow down")
elif light=="green":
    print("go")
else:
    print("i do't know the traffic light type!")
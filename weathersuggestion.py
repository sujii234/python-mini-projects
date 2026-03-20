#weater suggestion
weather= input("enter the weather (sunny, rainy cloudy):").lower()
if weather=="sunny":
    print("wear sunglasses")
elif weather=="rainy":
    print("take an umbrella")
elif weather=="cloudy":
    print("wear a jacket")  
else:
    print("i do't know the weather type")
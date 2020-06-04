cars = {
    "Tesla Model 3 LR": [310, 49900],
    "Hyundai Ioniq EV": [124, 30315],
    "Chevy Bolt": [238, 36620]}

# You could add as many cars to the dictionary above and this will work.
# Above, is a dictionary where the keys are car models, and the sub-lists contain the range and price respectively.

for key in cars.keys():
    
        if cars[key][0] >= 200 and cars[key][1] >=40000:
            print("{} has good range but is expensive".format(key))
        elif cars[key][0] <= 200 and cars[key][1] >=40000:
            print("{} has bad range and is expensive".format(key))

        elif cars[key][0] >= 200 and cars[key][1] <= 40000:
            print("{} has good range and is affordable".format(key))

        else:
            print("{} has bad range but is affordable".format(key))

            
            

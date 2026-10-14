distance_mi = 20
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

#**MY CODE**#
#number 5
if not distance_mi:
    print("False")

#number 6
if distance_mi <= 1:
    is_raining == False
    print("True")
else:
    print("False") 

#number 7
if distance_mi > 1 and distance_mi <= 6:
    has_bike == True and is_raining == False
    print("True")
else:
    print("False")

#number 8
if distance_mi > 6: 
    has_car == True 
    print("True")
elif has_ride_share_app == True:
    print("True")
else:
    print("False")


#**SOLUTION**

if not distance_mi:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)
else:
    print(False)
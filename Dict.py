pop = [30.55, 2.77, 39.21]
countries = ["Afganistan","ALbania","Algeria"]
world = {"Afganistan": 30.55,"Albania":2.77,"Algeria":39.21}
print(world["Albania"])
"""pencarian kunci harusunik, jika ditambah Albania:2.81 maka yang diambil nilai paling akhir"""

world = {"Afganistan": 30.55,"Albania":2.77,"Algeria":39.21, "Sealand":0.0000028}
del(world["Sealand"])
print(world)

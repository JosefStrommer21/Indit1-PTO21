import math

winkel_grad = 0

while winkel_grad <= 180:
    winkel_rad = winkel_grad * math.pi / 180
    cosinus = math.cos(winkel_rad)
    print("Winkel : " , winkel_grad, "-> cosinus: ", cosinus)
    winkel_grad += 10
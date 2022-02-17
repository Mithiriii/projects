import math

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0,0158

#stwierdzenie o przedziałach ufności odnosi się do przedziału a nie samej wartości p, należy to rozumieć tka
#że w 95% przypadków wyrzucony parametr znajdowałby się w przedziałach ufności
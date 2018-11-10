x = 3
y = 4
b = -10
learning_rate = 0.1

print(x * 1 + y * 1 + b)
i = 1
while x * 1 + y * 1 + b <= 0:
    x += learning_rate
    y += learning_rate
    b += learning_rate
    print(i, " ", x, " ", y, " ", b, " ", x * 1 + y * 1 + b)
    i += 1

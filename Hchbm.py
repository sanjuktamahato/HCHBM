import random


def f(x):
    return - (x - 3) ** 2 + 9


step_size = 0.5


x = random.uniform(0, 6)
current_value = f(x)

print("Initial x:", round(x, 2), "Initial f(x):", round(current_value, 2))

while True:
    
    left = x - step_size
    right = x + step_size

    
    if left < 0:
        left = 0
    if right > 6:
        right = 6

    
    left_value = f(left)
    right_value = f(right)

    
    if left_value > current_value:
        x = left
        current_value = left_value
    elif right_value > current_value:
        x = right
        current_value = right_value
    else:
        
        break

print("Final x:", round(x, 2), "Final f(x):", round(current_value, 2))



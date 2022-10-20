import motors

motor = motors.Motors()

for i in range(1, 30):
    motor.left(i/10)
    motor.right(i/10)

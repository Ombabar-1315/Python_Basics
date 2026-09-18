import math
import random
import statistics

marks = [70, 85, 90, 65, 80]

average = statistics.mean(marks)
square = math.sqrt(average)
random_marks = random.choice(marks)

print("Marks:", marks)
print("Average:", average)
print("Square Root of Average:", square)
print("Randomly Selected Mark:", random_marks)
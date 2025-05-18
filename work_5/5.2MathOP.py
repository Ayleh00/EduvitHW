import random
import math
import statistics as stats


numbers = [random.randint(1, 100) for i in range(100)]


mean_value = stats.mean(numbers)         
median_value = stats.median(numbers)      
stdev_value = stats.stdev(numbers)      
sqrt_sum = round(math.sqrt(sum(numbers))) 


print(f"Среднее: {mean_value}", f"Медиана: {median_value} ", f"Стандартное отклонение: {stdev_value}", f"корень из суммы: {sqrt_sum}")

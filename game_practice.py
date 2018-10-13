import random
months = (1,2,3,4,5,6,7,8,9,10,11,12)
days = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
random_month = random.choice(months)
random_day = random.choice(days)
# issues with what I have done so far:
        # not returned as date format
        # I can get dates like 6/31 or 2/30 that DNE

print(random_month, "/", random_day)


# Let's do some statistics
import statistics
average = statistics.harmonic_mean(days)
print(average)

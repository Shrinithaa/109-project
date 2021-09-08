import random
import statistics
import plotly.figure_factory as pff
diceResult = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)

mean = sum(diceResult)/len(diceResult)
stdDeviation = statistics.stdev(diceResult)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)
print('Mean is: ', mean)
print('Standard Deviation is: ', stdDeviation)
print('Median is: ', median)
print('Mode is: ', mode)

fig = pff.create_distplot([diceResult],['Result'],show_hist= False)
fig.show()


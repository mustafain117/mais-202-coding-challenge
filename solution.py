import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv') as file:
    datafile = csv.DictReader(file)
    
    purposes = ['car', 'credit_card', 'debt_consolidation', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'small_business', 'vacation', 'wedding']
    sum_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for line in datafile:
        index = purposes.index(line['purpose'])
        sum_list[index] = sum_list[index] + float(line['int_rate'])
        freq[index] = freq[index] + 1

i = 0
while i < len(purposes):
    average[i] = round(sum_list[i]/freq[i], 3)
    i+= 1

answer=np.column_stack((purposes,average))
print(answer)

chart = plt.bar(purposes, average)
plt.xlabel('purpose')
plt.ylabel('mean(int_rate)')
plt.tick_params(axis='x', labelsize=6)

chart[0].set_color('seagreen')
chart[1].set_color('coral')
chart[2].set_color('grey')
chart[3].set_color('hotpink')
chart[4].set_color('yellow')
chart[5].set_color('gold')
chart[6].set_color('wheat')
chart[7].set_color('silver')
chart[8].set_color('seagreen')
chart[9].set_color('coral')
chart[10].set_color('grey')

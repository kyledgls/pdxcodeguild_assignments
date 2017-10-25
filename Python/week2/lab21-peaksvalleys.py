"""
This program identifies and stores and displays the peaks and valleys in data
"""




print('welcome to peaks and valleys ')

#begins the function
def peaks_and_valleys(data):
    # identifies the lists
    x = []
    y = []
    # loops to check for certain data conditions for peaks
    for i in range(1, len(data)-1):
        if data[i - 1] < data[i] > data[i + 1]:
            x.append(i)
            #print('peaks:', x, i)
    # loops to check for certain data conditions for valleys
        elif data[i -1] > data[i] < data[i + 1]:
            y.append(i)
            #print('valleys:',y, i)
# tuple return
    return x, y

# data list
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# unboxes the tuple
peaks, valleys = peaks_and_valleys(data)
# prints x and y
print('peaks: ', peaks)
print('valleys: ', valleys)


for i in range(1, len(data)):







#
# x = []
# for i in range(1, 11):
#     x = []
#     x.append('x'*i)
#     print(x)
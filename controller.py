import greedyAlgorithm
# reading input file inputPS1.txt
input = open("inputPS1.txt","r")
modified_input = []
for line in input:
    breakup = line.strip().split("/")
    for i in range(0, len(breakup)):
        breakup[i] = int(breakup[i])
    modified_input.append(breakup)
# for i in modified_input:
#     i.append((i[1]+i[2])/2)
instance = greedyAlgorithm.greedyAlgorithm()
x = instance.sorting(modified_input)
# y = [[2, 1, 2], [4, 5, 4], [1, 5, 8], [3, 8, 2]]
# instance.calculate(x)
# instance.calculate(y)
manufacturing, assembling = instance.calculate(x)
# print(manufacturing)
# print(assembling)
count = 0
for i in range(0, len(assembling)):
    if assembling[i] == 0:
        count += 1
print(count)
order = []
for i in range(0, len(manufacturing)):
    if manufacturing[i] not in order:
        order.append(manufacturing[i])
print(order)

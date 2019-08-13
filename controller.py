import greedyAlgorithm
# reading input file inputPS1.txt
input = open("inputPS1.txt","r")
modified_input = []
for line in input:
    breakup = line.strip().split("/")
    modified_input.append(breakup)
for i in modified_input:
    i.append((int(i[1]) + int(i[2])) / 2)
    # print(i)
instance = greedyAlgorithm.greedyAlgorithm()
x = instance.sorting(modified_input)
y = [['2', '1', '2', 1.5], ['4', '5', '4', 4.5], ['3', '8', '2', 5.0], ['1', '5', '7', 6.0]]
instance.calculate(x)
import greedyAlgorithm
# reading input file inputPS1.txt
input = open("inputPS1.txt","r")
modified_input = []
for line in input:
    breakup = line.strip().split("/")
    for i in range(0, len(breakup)):
        breakup[i] = int(breakup[i])
    modified_input.append(breakup)
    
instance = greedyAlgorithm.greedyAlgorithm()
x = instance.quick_sort(modified_input)

manufacturing, assembling = instance.calculate(x)

count = 0
for i in range(0, len(assembling)):
    if assembling[i] == 0:
        count += 1
order = []
for i in range(0, len(manufacturing)):
    if manufacturing[i] not in order:
        order.append(manufacturing[i])
print("Mobiles should be produced in the order: " + str(order)[1:-1]) 
print("Total production time for all mobiles is: " + str(len(assembling)))
print("Idle Time of Assembly unit: " + str(count))
f = open("outputPS1.txt", "w")
f.write("Mobiles should be produced in the order: " + str(order)[1:-1] +"\n")
f.close()
f = open("outputPS1.txt", "a")
f.write("Total production time for all mobiles is: " + str(len(assembling))+"\n")
f.write("Idle Time of Assembly unit: " + str(count))
f.close()

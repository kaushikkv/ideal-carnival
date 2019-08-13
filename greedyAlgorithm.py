def sortSecond(val):
    print(val[1])
    return val[1]

class greedyAlgorithm:
    def __init__(self):
        pass



    def sorting(self, modified_input):
        process1 = sorted(modified_input, key = lambda x: x[1])
        # print(process1)
        return process1

    def calculate(self, sorted_list):
        manufacturing = []
        assembling=[]
        for i in range(0, len(sorted_list)):
            for j in range(0, int(sorted_list[i][1])):
                manufacturing.append(sorted_list[i][0])
            for k in range(0, (len(manufacturing)-len(assembling))):
                assembling.append(0)
            for j in range(0, int(sorted_list[i][2])):
                assembling.append(sorted_list[i][0])
        # print(manufacturing)
        # print(assembling)
        return manufacturing, assembling

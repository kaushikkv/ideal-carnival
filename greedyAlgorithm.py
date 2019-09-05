def sortSecond(val):
    print(val[1])
    return val[1]

class greedyAlgorithm:
    def __init__(self):
        pass



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

    def partition(self, nums, low, high):
        # We select the middle element to be the pivot.
        pivot = nums[(low + high) // 2][1]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i][1] < pivot:
                i += 1

            j -= 1
            while nums[j][1] > pivot:
                j -= 1
    
            if i >= j:
                return j
    
            # If an element at i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot), then swap them
            nums[i], nums[j] = nums[j], nums[i]


    def quick_sort(self, nums):
        # Create a helper function that will be called recursively
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = self.partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)
    
        _quick_sort(nums, 0, len(nums) - 1)
        return nums

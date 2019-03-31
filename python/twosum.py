class Solution:
    def twoSum(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
        """
        total = int(target)
        mylist = nums
        length = len(mylist)
        i = 0
        j = 1
        answer = []
        for value in mylist:
            # print(i)
            j = i + 1
            while j < length:
                # print(j)
                if value + mylist[j] == total:
                    answer = [ i, j]
                    print(i, j)
                    # return(result)
                # print(i,j)
                j += 1
            i += 1
        return answer

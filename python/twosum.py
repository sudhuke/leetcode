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
        #print(length+target)
        number = 0
        while number < length:
            if int(mylist[number]) < total:
                #print(mylist[number] + " is less than " + total)
                search_number=total - int(mylist[number])
                #print(search_number)
                if search_number in mylist:
                    new_index=mylist.index(search_number)
                    # print(new_index + search_number)
                    if new_index > number:
                        #print(number + new_index)
                        answer=[number,new_index]
            number=number + 1
        return answer

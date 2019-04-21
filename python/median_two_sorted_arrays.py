class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        newlist = []
        for item in nums1:
            newlist.append(item)

        for item in nums2:
            newlist.append(item)

        newlist.sort()
        length = len(newlist)
        check_length = length % 2
        if check_length != 0:
            median_no = length / 2
            median = newlist[int(median_no)]
        else:
            right_index = int( length / 2 )
            left_index = int(right_index) - 1
            left_index_value = int(newlist[left_index])
            right_index_value = int(newlist[right_index])
            median = (left_index_value + right_index_value ) / 2

        return float(median)

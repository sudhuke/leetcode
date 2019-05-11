class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        count=1
        location=0
        match_length=1
        matched=False
        longest_palin=""
        for location in range(length):
            while count <= length:
                search_str=s[location:count]
                rev_search_str=search_str[::-1]
                len_search_str=len(search_str)
                if search_str == rev_search_str and len_search_str >= match_length:
                    match_length=len_search_str
                    longest_palin=search_str
                count=count + 1
            location=location +1
            count=location + 2
        return longest_palin

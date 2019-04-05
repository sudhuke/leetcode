class Solution:
    def lengthOfLongestSubstring(self, str):
        mystring = str
        length = len(mystring)
        print(length)
        count = 0
        next_count = 1
        string_list = list(mystring)
        if length == 0:
            return 0
        substring = mystring[0]
        final_list = []
        for current_character in string_list:
            # print("checking for character : " + current_character)
            if count < length:
                # substring += current_character
                if count + 1 == length:
                    next_character = mystring[count]
                else:
                    next_character = mystring[count+1]
                    # print("next character would be : " + next_character)
                    # print("Index of character : ")
                    # print(count)
                if current_character == next_character and count != length:
                    # Same character found
                    substring = ""
                    # print("Resetting the substring  ..." + substring)
                    final_list.append(current_character)
                    count += 1
                    continue
                else:
                    # if next_character not in substring:
                    if substring == "":
                        substring += current_character + next_character
                    else:
                        if next_character in substring and substring.index(next_character) < count:
                            # print("Found a character: " + next_character +" in substring : " + substring)
                            substring = substring[substring.index(next_character)+1:]+next_character
                        else:
                            substring += next_character
                    count += 1

            #    print("Appended the string : "+substring)
            final_list.append(substring)
        # print(final_list)
        result = max(final_list, key=len)
        # print(len(result))
        return len(result)

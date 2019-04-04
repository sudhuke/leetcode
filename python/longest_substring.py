string=input("Enter a string")
length=len(string)
print(length)
count=0
next_count=1
string_list = list(string)
substring = string[0]
final_list = []
for current_character in string_list:
    print("checking for character : " + current_character)
    if count < length:
        #substring += current_character
        if count + 1 == length:
            next_character = string[count]
        else:
            next_character = string[count+1]
        print("next character would be : " + next_character)
        print("Index of character : ")
        print(count)
        if current_character == next_character and count != length:
        # Same character found
            final_list.append(substring)
            substring = ""
            print("Resetting the substring  ..." + substring)
            count += 1
            continue

        else:
            # if next_character not in substring:
                if substring == "":
                    substring += current_character + next_character
                else:
                    if next_character in substring:
                        substring += current_character
                    else:
                        substring += next_character

    print("Appended the string : "+substring)
    count += 1
for entry in final_list:
    print(entry)











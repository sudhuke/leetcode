class Solution:
    def reverse(self, x: int) -> int:
        number=str(x)
        first_char=number[0]
        number_string = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        highest_number = 2**31 - 1
        base_number = -2**31
        first_digit=False
        print(highest_number)
        for each_number in number_string[:]:
            if str(each_number) == str(first_char):
                print("First digit is number only")
                first_digit = True
            if first_digit is True:
                new_number=number[::-1]
            else:
                new_number=number[1::]
                new_number=new_number[::-1]
    #new_number=first_char+new_number

        if int(new_number) > highest_number or int(new_number) < base_number:
            result=0
        else:
            reversed_number=new_number 
            if first_digit is False:
                result=first_char + reversed_number
            else:
                result=reversed_number
        return int(result)

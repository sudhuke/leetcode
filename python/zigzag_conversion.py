class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string=s
        no_rows = numRows
        str_length=len(s)
        row=0
        newstring = []
        no_col=no_rows - 2
        eachrow = 0
        length = 0
        finalstring=""
        while length < str_length:
            for eachrow in range(no_rows):
                if length < str_length:
                    newstring.append([])
                    newstring[eachrow].append(string[length])
                length = length + 1
                eachrow = eachrow + 1
                #print(newstring)
            if eachrow == no_rows:
                eachrow = eachrow - 2
            while eachrow > 0:
                if length < str_length:
                    newstring[eachrow].append(string[length])
                length = length + 1
                eachrow = eachrow - 1
        for list in newstring[:]:
            for eachchar in list[:]:
                finalstring+=eachchar
        print(finalstring)
        return finalstring
        

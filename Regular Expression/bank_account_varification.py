import re 

with open("banks.txt","r") as f1:
    
    for lines in f1:

        pattern  =  "(SBIN|HDFC|ABCD|ICICI)[0-9]{7}[0-9]{9,18}" 
        #"|(HDFC)0000[0-9]{18}|(ABCD)[0-9]{15}|(ABCD)[0-9]{15})"
            
        lines = lines.rstrip("\n")

        print(lines)

        matches =  re.fullmatch(pattern,lines)

        print(matches)

        if matches:

            bank = lines[:5]

            if bank == "SBIN":

                with open("sbin.txt","w") as f2:
                    
                    f2.write(f"{lines}\n")

            elif bank == "ICICI":

                with open("icici.txt","w") as f3:
                   
                    f3.write(f"{lines}\n")

            elif bank == "HDFC":
                    
                with open("hdfc.txt","w") as f4:
                         
                    f4.write(f"{lines}\n")

            elif bank == "ABCD":
                     
                with open("ABC.txt","w") as f5:
                         
                    f5.write(f"{lines}\n")
                         




# add all .com urls to com_url.txt using regular expression


import re 

with open("domain.txt","r") as f1:

    with open("com_url.txt","w") as f2:

        pattern = r'^(https?://)?(www\.)?.+\.com$'

        for lines in f1:
              
              lines=lines.rstrip("\n")

              matches = re.fullmatch(pattern,lines)

              if matches:
                   
                   f2.write(f"{lines}\n")


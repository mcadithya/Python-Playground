with open("people.txt","r") as f1:

    with open("eligible_for_voting.txt","w") as f2:

        with open("not_eligible.txt", "w") as f3:


            for lines in f1:

                lines=lines.rstrip("\n")

                name,age = lines.split(",")

                print(name,age)

                if int(age)>=18:

                    f2.write(f"{name}\n")

                else:

                    f3.write(f"{name}\n")
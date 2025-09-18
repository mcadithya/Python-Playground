# first class object 
# 
# you can assign to a variable 
# 
# you can send as function argument
# 
# return using return keyword 
# 
# 
# eg: str(),int() -- datatypes, all functions
# for function standerd form fn or func

def divorce(fn):

    def wrapper(name,age,marital_status,behaviour):

        age = 29

        marital_status = "divorced"

        behaviour = ["lazy person","not go for job", "irrespondsible","gym"]
         
        return fn(name,age,marital_status,behaviour)
    return wrapper


def marriage(fn):

    def wrapper(name,age,marital_status,behaviour):

        marital_status = "married"

        behaviour = ["responsible","not go for job"]

        return fn(name,age,marital_status,behaviour)

    return wrapper



@marriage
@divorce
def john(name,age,marital_status,behaviour):

    print(name)

    print(age)

    print(marital_status)

    print(behaviour)

john("john",27,"single",["lazy person","not go for job", "irrespondsible"])
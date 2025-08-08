nominees = ["Lee", "Irene","Lee", "Irene","Lee", "Irene","Mercy"]

# List comprehension
# Writing a list object in one line to avoid repetitive code and using a for loop.
# a way to loop through every item of an array in one line and return another array

# loop through nominees and return another list with  ["VOTE RECORDED FOR LEE, VOTE RECORDED FOR IRENE"]

# return_list = []
# for nominee in nominees:
#     vote_string = f"VOTE RECORDED FOR {nominee}"
#     return_list.append(vote_string)

# print(return_list)


# return_list = [operation, forloop]
# return_list = [operation on item for item in original list]
return_list = [f'Vote Recorded For {nominee}' for nominee in nominees if nominee == "Mercy"] #the final list for vote records
print(return_list)
print(nominees)
# vote_string = "" #something like this VOTE RECORDED FOR LEE











contestants = set(nominees)

print(contestants)

def foo():
    return "vvvv"

random_list = ["Kaynan", foo, {"name":"Mercy", "occupation":"Dev"}]


student_data = {"name":"Mercy", "occupation":"Dev"}
print(student_data['occupation'])



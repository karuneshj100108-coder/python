# students in exams
cet = {"Karunesh", "Bob"}
jee = {"Krushna", "Bob"}
neet = {"Hrugved", "Eve"}
print("All students:", cet|jee|neet) #Union
print("Students in all exam:", cet & jee & neet) # intersection
print("Cet but not in jee:", cet - jee) #Difference

sentence = "I heard the pastor sing live verses easily." #input("Enter a scentence: ")
sentence = sentence.lower()

separated = []
separated = sentence.split(" ")

final = ""

for i in range(len(separated) - 2):
    match = False
    toCondense = 0
    for letter in separated[i]:
        if separated[i][-(letter + 1)] == separated[i + 1][letter]:
            toCondense += 1
    if toCondense != 0:





# if match:
#     put words together
# else:
#     add word to final plus a space




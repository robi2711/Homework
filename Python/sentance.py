import random


dictionary = {
    'articles': ["the", "a", "one", "some", "any"],
    'nouns': ["teacher", "student", "principal", "library", "school"],
    'verbs': ["taught", "learned", "read", "walked", "ran"],
    'prepositions': ["to", "from", "over", "under", "on"],
    }
v = ['articles', 'nouns', 'verbs', 'articles', 'nouns', 'prepositions', 'verbs']
a = 0
myList = []
while a != 7:
    b = random.randint(0, 4)
    myList.append(dictionary[v[a]][b])
    a += 1
print(myList[0:])

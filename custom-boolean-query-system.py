'''file = I like onions very much. I  like onions on my sandwich and celery on the side. I  like cheese on my onions. Moreover, onions make my eyes water. My favorite cheese is cheddar. I want cheese and onions on my pizza.'''


file =  input("Enter the list of sentences to search in: ")

query = input("Enter the query to search: ")


def OR(s1,s2,s):
    return ((s1 in s)or(s2 in s))
def AND(s1,s2,s):
    return ((s1 in s)and(s2 in s))
def NOT(s1,s):
    return (not s1 in s)

        
sentence = list(file.split(". "))

if (query.startswith('NOT')) :
    buff =list(query.split())
    for sen in sentence:
        for i in range(0,len(buff),2):
            if buff[i] == 'NOT' :
                result = bool(NOT(buff[i+1],sen))
                if result == True:
                    print(sen)
            else:
                print("Enter correct query")
else:
    buff =list(query.split())
    for sen in sentence:
        for i in range(1,len(buff),2):
            if buff[i] == 'AND' :
                result = bool(AND(buff[i-1],buff[i+1],sen))
                if result:
                    print(sen)         
            elif buff[i] == 'OR':
                result = bool(OR(buff[i-1],buff[i+1],sen))
                if result:
                    print(sen)
            elif buff[i] == 'NOT' :
                result = bool(NOT(buff[i+1],sen))
                if ((buff[i-1]in sen) and result):
                    print(sen)
            else:
                print("Enter correct query")
                
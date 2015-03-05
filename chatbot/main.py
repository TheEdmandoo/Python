file = open("stopwords.txt")
stopwords = file.readlines()

for word in stopwords:
    next = word.strip()
    print(next)

name = " "    

def binstop(message):
    for word in stopwords:
        rubbish = word.strip()
        message = message.replace( " " + rubbish + " ", " ")
    message = message.replace( " name " , " ")
    return message

while True:

    input = raw_input("Hello, Whats your name?: ")
    input = " " + input + " "
    name = binstop(input)
    print("hello " + name.strip() + " im chatbot")

    input = raw_input("Whats your mood today " + name + "?")
    input = " " + input + " "
    print("Good to hear " + name.strip() + ", I feel the same")
    
    input = raw_input("Do you ever feel," + name + "like a plastic bag?")
    input = " " + input + " "
    print("I see")
    
    input = raw_input("Do you like Katy Perry," + name + "?")
    input = " " + input + " "
    print("I understand, I suppose shes ok.")
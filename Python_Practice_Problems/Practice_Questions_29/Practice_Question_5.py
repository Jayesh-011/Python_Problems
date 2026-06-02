import string       # for removing punctuations
import os

def freq(fname,text):
    ret = False 

    ret = os.path.exists(fname)
    if not ret:
        print("No such file")
        return

    content = str()
    cnt = 0

    f = open(fname,"r")

    content = f.read()
    f.close()

    content = content.split()
    print(content)
    content = [word.strip(string.punctuation) for word in content]

    print(content)
    
    '''
    We can also use lib nltk
    nltk.word_tokenize(string as input)
    but the replace is better for custom symbols as we can eliminate any we want
    and more better than replace is string.punctuation
    '''
    
    for words in content:
        if words == text:
            cnt = cnt + 1

    return cnt

def main():
    fname = str()
    word = str()
    count = 0

    fname = input("Enter file name :")
    word = input("Enter the string :")

    count = freq(fname=fname,text=word)

    print(f"The frequency of the word {word} is : {count}")

if __name__ == "__main__":
    main()
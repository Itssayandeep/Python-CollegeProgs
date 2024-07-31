def sentence_Palindrome(s):
    cleaned_sentence = ''.join(char.lower() 
    for char in s 
    if char.isalnum())
    return cleaned_sentence == cleaned_sentence[::-1]
def number_palindrome(s):
    temp=int(s)
    ans=0
    while(temp):
        digit=temp%10
        ans=ans*10+digit
        temp//=10
    return int(s)==ans
s= input("Enter a sentence/number: ")
if(s.isalpha()):
    if sentence_Palindrome(s):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")
else:
    if number_palindrome(s):
        print(s," is a palindrome.")
    else:
        print(s,"is not a palindrome.")

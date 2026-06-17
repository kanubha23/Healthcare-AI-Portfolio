#defining the function convert to convert emoticons into emojis
def convert(abx = ":)"):
    #Creating a dictionary to store the emoticons and their corresponding emojis
    
        abx = abx.replace(":)", "🙂")
        abx = abx.replace(":(", "🙁")
        abx = abx.replace(";)", "😉")
        return abx
    


#defining the main function
def main():
    text = input("Enter a message: ")
    print(convert(text))




    
main()
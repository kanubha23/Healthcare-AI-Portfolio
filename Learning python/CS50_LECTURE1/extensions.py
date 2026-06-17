#Asking the user to enter the name of the file to be opened
filename = input("Enter the name of the file to be opened: ")
#taking the file name, splitting it into the extension and the rest of the name, then converting the extension into lower case. 
fileextension = filename.split(".")[-1].lower()

if fileextension == "gif" or fileextension == "jpg" or fileextension == "jpeg" or fileextension == "png":
        print("Image/", fileextension)
elif fileextension == "pdf" or fileextension == "txt" or fileextension == "zip":
        print("Application/", fileextension)
else :
    print("Unknown")
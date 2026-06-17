def main():
#Asking the user what is the time
   time= input("What is the time? ")
   t = convert(time)
   if t >= 7 and t <= 8:
        print("breakfast time")
   elif t >= 12 and t <= 13:
                print("lunch time")
   elif t >= 18 and t <= 19:
                print("dinner time")    



def convert(time):
   t = time.split(":")
   hour = int(t[0])
   minute = int(t[1])
   return hour + minute / 60
 





main()


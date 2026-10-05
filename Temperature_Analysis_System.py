import numpy as np
print("\n-----------Temperature Analysis System-------------")

tem= np.array([["City", "Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
              ["Tokyo",    32    ,   23    ,    36     ,     31    ,    27   ,    26     ,   32   ],
              ["Chennai",   43   ,   32    ,    39     ,     32    ,    21   ,    32     ,   27   ],
              ["los angeles", 37 ,   38    ,    36     ,     29    ,    32   ,    21     ,   27    ],
              ["Beijing" ,   26  ,   25    ,    24      ,    28    ,    24    ,   30     ,   -15, ]])


while True:
    try:
       menu= input("\n 1. Show the temperatures for 7 days and 4 different cities \n 2. Average temperature of each city \n 3. Hottest temperature recorded \n 4. Coldest temperature recorded \n 5. Temperature above 35°C  \n 6. Add different city and it's temperature \n 7. Exit \n  ")
   


       if menu=="1":
        print("================ TEMPERATURES OF CITIES ===================")
        print(tem) 
        save = input("Do you want to save this in saperate file?(yes/no)")
        if save=="yes":
            with open("cities.txt", "w") as f:
                f.write(str(tem))
                print("file saved Successfully!")

        else:
            continue
       elif menu =="2":
           User_input=input("Enter the city :- ").strip().title()
           citys= tem[1:,0]
           avg = np.where(citys== User_input)[0]
           if len(avg) == 0:
               print("City not found!")

           else:
              tem_index= avg[0]

              avg_of_city =np.mean(

                 tem[1:, tem_index  + 1].astype(int)

              )
              print(f" Average temperature of {User_input} is {avg_of_city}°C  ") 
 
       elif menu =="3":
          hottest= np.max(tem[1:,1:].astype(int))
          print(f" The Hottest temperature recorded was {hottest}°C ")
       
       elif menu=="4":
          coldest = np.min(tem[1:,1:].astype(int))
          print(f" The coldest temperature recorded was {coldest}°C ")

        
       elif menu=="5":
          above_thirty_five= tem[1:,1:].astype(int)[tem[1:,1:].astype(int)>35]
          print(f"Temperature above 35°C {above_thirty_five}")

        
       elif menu=="6":

           user_input=input("Enter the city :- ").strip().title()
           
           rng = np.random.default_rng()
           rang_tem = rng.integers(low= -14 , high=55, size=7)
           new_tem= np.concatenate((np.array([user_input]), rang_tem.astype(str)))
           tem= np.vstack((tem,new_tem))
        #new_tem= np.append(tem,[[4,8]], axis=0 )
           print("New City added Successfully!")
           print(new_tem)


       elif menu=="7":

           user_exit=input("Do you want to exit?(yes/no)")
           if user_exit=="yes":
               print("Exiting.........")
               break
           else:
               continue
    
    except ValueError:
       print("You entered a invalid number.")

    
    except Exception as e:
       print(f"Something went wrong {e}")
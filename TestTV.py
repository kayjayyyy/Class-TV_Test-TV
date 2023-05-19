# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 6 - Class TV_Test TV

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(85))

from ClassTV import TV

# Assign tv1 and tv2
tv1 = TV
tv2 = TV

def TestTV():
    
    # Television 1 title and loading banner
    print("\n")
    print("\033[1mT E L E V I S I O N  1\033[0m".center(85))
    print("")
    print("\033[31m-\033[0m" * 80)
    print("\033[1;3;32mLoading..........\033[0m".center(90))
    print("\033[31m-\033[0m" * 80)
    
    # Assign value for tv1
    tv1 = TV(30, 3, True)
    
    # Print the television 1 outcome
    print("\n\033[36;1mtv1's channel is", tv1.getChannel() , "and volume level is", tv1.getVolume(), "\033[0m")
        
    print("\n")
    print("⨉ " * 40)
    
    # Television 2 title and loading banner
    print("\n")
    print("\033[1mT E L E V I S I O N  2\033[0m".center(85))
    print("")
    print("\033[31m-\033[0m" * 80)
    print("\033[1;3;32mLoading..........\033[0m".center(90))
    print("\033[31m-\033[0m" * 80)
    
    # Assign value for tv2
    tv2 = TV(3, 2, True)
    
    # Print the television 2 outcome
    print("\n\033[36;1mtv2's channel is", tv2.getChannel() , "and volume level is", tv2.getVolume(), "\033[0m")
    print("")
    
TestTV()

# Outro and border line
print("\n")
print("\033[3mThank you! Have a great day!".center(80))
print("")
print("\033[35m※ \033[0m" * 40)
print("")
# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 6 - Class TV_Test TV

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome! ♥ \033[0m".center(85))

from ClassTV import TV

def TestTV():
    
    print("")
    print("-" * 70)
    print("\033[1;3;32mProcessing..........\033[0m".center(80))
    print("-" * 70)
    
    tv1 = TV(30, 3, True)
    print("tv1's channel is", tv1.getChannel, "and volume level is", tv1.getVolume)
    
TestTV()
    
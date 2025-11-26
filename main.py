
import random
lowercase_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','x','w','z']
uppercase_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','X','W','Z']
special_characters = ['&','é','"','#','{','(','[','-','|','è','`','_','ç','^','à','@','°',']',')','+','=','}','¨','$','£','¤','*','µ','ù','%','!','§',':','/',';','?','.',',','<','>']
digit_characters = ['1','2','3','4','5','6','7','8','9','0']

print("""                                                                                                                                                     
 _______  _______  _______  _______           _______  _______  ______     _______  _______  _        _______  _______  _______ _________ _______  _______  
(  ____ )(  ___  )(  ____ \(  ____ \|\     /|(  ___  )(  ____ )(  __  \   (  ____ \(  ____ \( (    /|(  ____ \(  ____ )(  ___  )\__   __/(  ___  )(  ____ )
| (    )|| (   ) || (    \/| (    \/| )   ( || (   ) || (    )|| (  \  )  | (    \/| (    \/|  \  ( || (    \/| (    )|| (   ) |   ) (   | (   ) || (    )|
| (____)|| (___) || (_____ | (_____ | | _ | || |   | || (____)|| |   ) |  | |      | (__    |   \ | || (__    | (____)|| (___) |   | |   | |   | || (____)|
|  _____)|  ___  |(_____  )(_____  )| |( )| || |   | ||     __)| |   | |  | | ____ |  __)   | (\ \) ||  __)   |     __)|  ___  |   | |   | |   | ||     __)
| (      | (   ) |      ) |      ) || || || || |   | || (\ (   | |   ) |  | | \_  )| (      | | \   || (      | (\ (   | (   ) |   | |   | |   | || (\ (
| )      | )   ( |/\____) |/\____) || () () || (___) || ) \ \__| (__/  )  | (___) || (____/\| )  \  || (____/\| ) \ \__| )   ( |   | |   | (___) || ) \ \__
|/       |/     \|\_______)\_______)(_______)(_______)|/   \__/(______/   (_______)(_______/|/    )_)(_______/|/   \__/|/     \|   )_(   (_______)|/   \__/ 
___________________________________________________________________________________________________________________________________________________________    """)
print("")

def main():
    """INPUT: "weak", "medium" or "strong"
    OUT: a new password"""
    selection = input("Which level of security is desired for your password? (weak/medium/strong): ").lower()

    if selection == 'weak':
        faible()
    elif selection == 'medium':
        moyen()
    elif selection == 'strong':
        solide()
    else:
        print("Invalid choice. Please choose between 'weak', 'medium', or 'strong' without the " ".")
        main()


def faible():
    password = ''.join(random.choices(lowercase_characters + uppercase_characters, k=5))
    print("")
    print("The generated password is:", password)
    print("")
    request = input("Did you want a other password (y/n): ")
    print("--------------------------------------------------")
    if request == 'y':
        main()
    else:
        return

def moyen():
    password = ''.join(random.choices(lowercase_characters + uppercase_characters + digit_characters, k=15))
    print("")
    print("The generated password is:", password)
    print("")
    request = input("Did you want a other password (y/n): ")
    print("--------------------------------------------------")
    if request == 'y':
        main()
    else:
        return

def solide():
    password = ''.join(random.choices(lowercase_characters + uppercase_characters + digit_characters + special_characters, k=21))
    
    print("\n""The generated password is:""\n", password )
    
    request = input("Do you want an other password (y/n): ")
    print("--------------------------------------------------")
    if request == 'y':
        main()
    else:
        return

if __name__ == "__main__":
    main()

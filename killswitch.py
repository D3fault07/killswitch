import requests
import os 
os.system('cls')

def check_killswitch():
    url = "%URL%"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        content = response.text.strip()
        if content.lower() == "on":
            print('killswitch Active program will exit')
            return False
        elif content.lower() == "off":
            return True
        else:
            print("unexpected content in the url.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error checking killswitch: {e}")
        return False

if not check_killswitch():
    print("exiting the program.")
    exit()
print("killswitch is not active")

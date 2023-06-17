#AUTHOR MICHAEL MARIANI - STUDENT NUMBER 4002416


import os

class MobileOS:
    
    #initialized the battery state to 100
    def __init__(self):
        self.battery_level = 100
        
    #displays the current battery level    
    def display_battery(self):
        print("Battery level: ", self.battery_level, "%") 
        
    #Takes an integer number as input, checks if it is 10 digits and starts with 04, if so it proceeds, otherwise displays an error message
    def make_call(self):
        mobile_number = input("Enter mobile number: ")
        if not mobile_number.isnumeric or len(mobile_number) != 10 or not mobile_number.startswith("04"):
            print("Error: Invalid mobile number")
            return
        if self.battery_level <= 5:
            print("Error: Battery level is too low, please charge")
        else:
            self.battery_level -= 5
            print("Now calling: " + mobile_number)
            self.display_battery()
            
    #takes a string as input, and checks to see if it is a valid email. Will either succeed or fail based on checks.        
    def send_email(self):
        email_address = input("Enter email address: ")
        if email_address.count("@") != 1 or "gmail.com" not in email_address.split("@")[1]:
            print("Error: Invalid email address")
            return
        if self.battery_level <= 10:
            print("Battery level is too low to perform this operation, please charge")
            return
        else:
            self.battery_level -= 10
            print("Email has been sent to: " + email_address)
            self.display_battery()
    
    #Charges the battery to 100%        
    def charge_battery(self):
        if self.battery_level < 100:
            self.battery_level = 100
            print("Battery recharged to 100%")
        else:
            print("Battery is already charged")
        
        self.display_battery()  
        
    #draws the menu   
    def draw_menu(self):
        print("[---------------------------------------]")
        print("                            BAT: ", self.battery_level, "%")
        print("│  1. Make a call                       │")
        print("│  2. Send an email                     │")
        print("│  3. Recharge the battery              │")
        print("│  4. Turn off phone                    │")
        print("[---------------------------------------]")
        
        
    #main loop, runs the menu and reads/acts according to input
    #also clears the screen as to not look messy in the terminal.    
    def main(self):
        sel = 0
        invalid_attempts = 0
        while True:
            self.draw_menu()
            sel = input("Please input a menu option 1-4: ")
            sel = int(sel)
            
            while sel not in range(1,5):
                if(invalid_attempts == 1):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.draw_menu()
                    invalid_attempts = 0
                print("Invalid input!")
                sel = input("Please input a menu option 1-4: ")
                sel = int(sel)
                invalid_attempts += 1
            os.system('cls' if os.name == 'nt' else 'clear')    
            if sel == 1:
                
                self.make_call()
            elif sel == 2:
                
                self.send_email()
            elif sel == 3:
                
                self.charge_battery()
            else:
                return False
            
            if self.battery_level == 0:
                return False
            
            
        
phone = MobileOS()
phone.main()

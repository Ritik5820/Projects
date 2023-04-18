import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
voice = engine.setProperty('voice',voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

import time
password ="4862"
balance = 2500

print("Welcome!\nPlease insert your card.")
speak("Welcome! Please insert your card.")
speak("aapka SBI bank me swagat hai. Kripiya apna card daale!")
time.sleep(10)

print("Hi, Please do not Remove your Chip Card.\nLeave your Card Inserted during the Entire Transaction.")
speak("Hi, Please do not Remove your Chip Card. Leave your Card Inserted during the Entire Transaction.")
speak("Kripiya apna card naa nikaaalna")
time.sleep(5)

print("Please Select Language\nPress 1 for English\nPress 2 for Hindi")
speak("Please Select Language. Press 1 for English. Press 2 for Hindi")
speak("Kripiya apni bhaashaa ko chooney. English ke liye 1 dabaaaye. Hindi ke liye 2 dabaaaye")

try:
    speak("Enter the number for your selected language.")
    speak("Kripiya apni bhaasha ka kramaank daaley.")
    lang = int(input("Enter the number for your selected language.\n"))
    if lang>2:
        print("Kindly enter the number of your selected language only.")
        speak("Kindly enter the number of your selected language only.")
        speak("Kripiya kramaank sahi se daaley.")
        # exit()

except Exception as e:
    print("Kindly enter the number of your selected language only.")
    speak("Kindly enter the number of your selected language only.")
    speak("Kripiya kramaank sahi se daaley.")
    # exit()

if lang==1:
    speak("Enter Any Number Between 10 and 99. For example 25")
    number = int(input("Enter Any Number Between 10 and 99\nfor eg.'25'\n"))
    if number>=10 and number<=99:
        speak("Please Enter Your PIN")
        pin = int(input("Please Enter Your PIN\n"))
        pin = str(pin)
        
        if len(pin)>len(password) or len(pin)<len(password):
            print("PIN should be of 4 digits only.\nPlease try again.")
            speak("PIN should be of 4 digits only. Please try again.")
        
        elif pin!=password:
            print("Invalid PIN")
            speak("Invalid PIN")
        
        else:
            speak("Welcome! Mister Ritik Kohad.")
            speak("Please Choose 'Banking' for Cash Withdrawal. Press 1 for BANKING, Press 2 for BALANCE INQUIRY, Press 3 for TRANSFER, Press 4 for REGISTRATION, Press 5 for MINI STATEMENT, Press 6 for SERVICES, Press 7 for QUICK CASH")
            first_options = int(input("Please Choose 'Banking' for Cash Withdrawal\nPress 1 for BANKING\nPress 2 for BALANCE INQUIRY\nPress 3 for TRANSFER\nPress 4 for REGISTRATION\nPress 5 for MINI STATEMENT\nPress 6 for SERVICES\nPress 7 for QUICK CASH\n"))
            if first_options==2:
                print(f"AVAILABLE BALANCE: {balance}\nThank You for using SBI.")
                speak(f"AVAILABLE BALANCE: {balance}. Thank You for using SBI.")
            
            elif first_options==1:
                speak("Please Select Transaction, Press 1 for FAST CASH, Press 2 for WITHDRAWAL, Press 3 for BALANCE INQUIRY, Press 4 for MINI STATEMENT, Press 5 for DEPOSIT, Press 6 for PIN CHANGE, Press 7 for OTHERS")
                second_options = int(input("Please Select Transaction\nPress 1 for FAST CASH\nPress 2 for WITHDRAWAL\nPress 3 for BALANCE INQUIRY\nPress 4 for MINI STATEMENT\nPress 5 for DEPOSIT\nPress 6 for PIN CHANGE\nPress 7 for OTHERS\n"))
                
                if second_options == 1:
                    speak("Please Select The Amount. 100, 200, 500, 1000, 2000, 3000, 5000, 10000")
                    quick_cash = int(input("Please Select The Amount\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                    speak("Press 1 for YES, Press 2 for NO")
                    quickCash_confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
            
                    if quickCash_confirmation == 1:
                        if quick_cash>balance:
                            print(f"Sorry!\nYou don't have {quick_cash} in your account.\nThank You for using SBI.")
                            speak(f"Sorry! You don't have {quick_cash} in your account. Thank You for using SBI.")
                        else:
                            balance = balance - quick_cash
                            print("Your Transaction is being Processed.\nPlease Wait..")
                            speak("Your Transaction is being Processed. Please Wait")
                            time.sleep(5)
                            print("Please Collect Cash And Take Your Card.")
                            speak("Please Collect Cash And Take Your Card.")
                            print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us")
                            speak(f"Transaction Complete. AVAILABLE BALANCE: {balance}. Thank You for banking with us")

                    else:
                        print("Trasaction is Cancelled.\nPlease Remove Your Card.\nThank You for using SBI")    
                        speak("Trasaction is Cancelled. Please Remove Your Card. Thank You for using SBI.")    


                elif second_options==2:
                    speak("Please Select Account Type. Press 1 for KCC, Press 2 for CURRENT, Press 3 for SAVINGS")
                    acc_type = int(input("Please Select Account Type\nPress 1 for KCC\nPress 2 for CURRENT\nPress 3 for SAVINGS\n"))
                    
                    if acc_type==2:
                        speak("Please Enter Amount. Cash Available, 100, 500, 200, 2000")
                        amount = int(input("Please Enter Amount.\n(Cash Available: Rs 100, Rs 500, Rs 200, Rs 2000)\n"))
                        speak("Press 1 for YES, Press 2 for NO")
                        confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
                        
                        if confirmation == 1:
                            if amount>balance:
                                print(f"Sorry! You Don't Have {amount} in your Account.\nThank You for using SBI")
                                speak(f"Sorry! You Don't Have {amount} in your Account. Thank You for using SBI.")
                            
                            else:
                                balance = balance - amount
                                print("Your Transaction is being Processed.\nPlease Wait..")
                                speak("Your Transaction is being Processed. Please Wait")
                                time.sleep(5)
                                print("Please Collect Cash And Take Your Card.")
                                speak("Please Collect Cash And Take Your Card.")
                                print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us")
                                speak(f"Transaction Complete. AVAILABLE BALANCE: {balance}. Thank You for banking with us")

                        else:
                            print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")
                            speak("Trasaction is Cancelled. Please Remove Your Card. Thank You for using SBI.")

                    else:
                        print("Wrong Account Type. Please Try Again.")
                        speak("Wrong Account Type. Please Try Again.")

                elif second_options == 3:
                    print(f"AVAILABLE BALANCE: {balance}\nThank You for using SBI.")
                    speak(f"AVAILABLE BALANCE: {balance}, Thank You for using SBI.")

                elif second_options == 5:
                    speak("Please select deposit transactions. Press 1 for DEPOSIT, Press 2 to CANCEL")
                    deposit_transaction = int(input("Please select deposit transactions.\nPress 1 for DEPOSIT\nPress 2 to CANCEL\n"))
                    if deposit_transaction == 1:
                        speak("Do not Deposit more than 200 Notes. You can Deposit upto 49900 only. Press 1 to CONFIRM, Press 2 to CANCEL")
                        depoTrans_confirmation = int(input("Do not Deposit more than 200 Notes.\nYou can Deposit upto Rs:49900 only.\nPress 1 to CONFIRM\nPress 2 to CANCEL\n"))
                        if depoTrans_confirmation == 1:
                            speak("Select Account Type. Press 1 for CURRENT, Press 2 for SAVINGS")
                            depoTransAcc_type = int(input("Select Account Type\nPress 1 for CURRENT\nPress 2 for SAVINGS\n"))
                            if depoTransAcc_type ==1:
                                speak("Acceptable denomination: 100, 200, 500, 2000, Please Insert Your Cash and Press 1 for Enter, or, Press 2 for CANCEL")
                                deposit = int(input("Acceptable denomination:\nRs 100\nRs 200\nRs 500\nRs2000\nPlease Insert Your Cash and Press 1 for Enter, or\nPress 2 for CANCEL\n"))
                                if deposit == 1:
                                    print("Please Wait...\nValidating the Cash...")
                                    speak("Please Wait. Validating the Cash...")
                                    time.sleep(5)
                                    print("Deposit Successful\nThank You for banking with us.")
                                    speak("Deposit Successful. Thank You for banking with us.")
                                
                                else:
                                    print("Transaction Cancelled.\nThank You for using SBI.")
                                    speak("Transaction Cancelled. Thank You for using SBI.")

                            else:
                                print("Sorry! You Don't have SAVINGS ACCOUNT.\nThank You for using SBI")
                                speak("Sorry! You Don't have SAVINGS ACCOUNT. Thank You for using SBI")

                        else:
                            print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI")
                            speak("Trasaction is Cancelled. Please Remove Your Card. Thank You for using SBI")
                    else:
                        print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI")
                        speak("Trasaction is Cancelled. Please Remove Your Card. Thank You for using SBI")

                else:
                    print("Sorry! Servers are under maintenance please try again later.")
                    speak("Sorry! Servers are under maintenance please try again later.")

            elif first_options == 7:
                speak("Please Select The Amount. 100, 200, 500, 1000, 2000, 3000, 5000, 10000")
                quick_cash = int(input("Please Select The Amount\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                speak("Press 1 for YES, Press 2 for NO")
                quickCash_confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
            
                if quickCash_confirmation == 1:

                    if quick_cash>balance:
                            print(f"Sorry!\nYou don't have {quick_cash} in your account.\nThank You for using SBI")
                            speak(f"Sorry! You don't have {quick_cash} in your account. Thank You for using SBI")
                    
                    else:
                        balance = balance - quick_cash
                        print("Your Transaction is being Processed.\nPlease Wait..")
                        speak("Your Transaction is being Processed. Please Wait..")
                        time.sleep(5)
                        print("Please Collect Cash And Take Your Card.")
                        speak("Please Collect Cash And Take Your Card.")
                        print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us.")
                        speak(f"Transaction Complete. AVAILABLE BALANCE: {balance}. Thank You for banking with us.")

                else:
                    print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI")
                    speak("Trasaction is Cancelled. Please Remove Your Card. Thank You for using SBI")
            
            else:
                print("Sorry! Servers are under maintenance please try again later.")
                speak("Sorry! Servers are under maintenance please try again later.")

    else:
        print("Please Enter Valid Number Between 10 and 99 Only.")
        speak("Please Enter Valid Number Between 10 and 99 Only.")

#############################################################################HINDI#########################################################################################################



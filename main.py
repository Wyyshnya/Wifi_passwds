import subprocess


# cp866 - кодировка русских cmd
def extract_wifi_passwords():
    try:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
        profiles = [i.split(':')[1].strip() for i in profiles_data if "All User Profile" in i]
    except UnicodeDecodeError:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
        profiles = [i.split(':')[1].strip() for i in profiles_data if "Все профили пользователей" in i]

    for profile in profiles:
        try:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8').split('\n')
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i]
        except UnicodeDecodeError:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(
                'cp866').split('\n')
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i]



        print(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')


extract_wifi_passwords()
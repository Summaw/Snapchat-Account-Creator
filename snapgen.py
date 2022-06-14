from pypasser import reCaptchaV3
import requests, random, string

checkUser = lambda user, cookies, xsrf_token: True if  requests.post('https://accounts.snapchat.com/accounts/get_username_suggestions',cookies=cookies ,data={'requested_username': user, 'xsrf_token': xsrf_token}).json()['reference']['status_code'] == 'OK' else False
def snapchat(user: str):
    if requests.get('https://accounts.snapchat.com/accounts/signup?client_id=ads-api&referrer=https%253A%252F%252Fads.snapchat.com%252Fgetstarted&ignore_welcome_email=true').url == 'https://www.snapchat.com/download': return {'ok': False, 'error': 'IP Blocked'}
    session = requests.session()
    randomVar = "".join([random.choice(string.digits + string.ascii_letters) for i in range(16)])
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    xsrf_token = session.get('https://accounts.snapchat.com/accounts/signup?client_id=ads-api&referrer=https%253A%252F%252Fads.snapchat.com%252Fgetstarted&ignore_welcome_email=true', headers=headers).cookies.get_dict()['xsrf_token'];cookies = session.cookies
    if checkUser(user, cookies, xsrf_token):
        response = session.post('https://accounts.snapchat.com/accounts/signup', headers=headers,
            data={'first_name': 'Alex', 'last_name': 'rain', 'username': user, 'password': f'x{randomVar}', 'birthday': '2000-04-01', 'email': f'y{randomVar}@gmail.com',
                    'xsrf_token': xsrf_token, 'g-recaptcha-response': reCaptchaV3("https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LezjdAZAAAAAD1FaW81QpkkplPNzCNnIOU5anHw&co=aHR0cHM6Ly9hY2NvdW50cy5zbmFwY2hhdC5jb206NDQz&hl=en&v=M-QqaF9xk6BpjLH22uHZRhXt&size=invisible&badge=inline&cb=9qlf8d10oqh9"),
                    'client_id': 'ads-api', 'referrer': 'https%3A%2F%2Fads.snapchat.com%2Fgetstarted', 'ignore_welcome_email': 'true'})
        if response.ok: return {'ok': True, 'error': None, 'results': {'user': user, 'password': f'x{randomVar}', 'email': f'y{randomVar}@gmail.com', 'birthday': '2000-01-31'}}
        else: return {'ok': False, 'error': 'Something went wrong'}
    else: return {'ok': False, 'error': 'Taken user'}

print("\n\n")
while True:
    user = input('Enter a user name: ')
    print(f'Results: {snapchat(user)}\n')

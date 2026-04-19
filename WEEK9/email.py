import re
import random
import string

teks = """anton@mail.com
budi@gmail.co.id
slamet@getnada.com
matahari@tokopedia.com"""

emails = re.findall(r'\S+@\S+', teks)

def generate_password():
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(8))

for email in emails:
    username = email.split("@")[0]
    password = generate_password()
    print(f"{email} username: {username}, password: {password}")
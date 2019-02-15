import random
import string

password=''.join(random.choice(string.punctuation + string.ascii_letters + string.digits) for _ in range(12))
print password

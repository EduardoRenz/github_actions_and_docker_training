import re
import os
from dotenv import load_dotenv
load_dotenv('.env')

environment = os.getenv('ENVIRONMENT')
print(f"running on {environment}")

def currency_format(value):
    is_int = re.search('[,|\. ]',value) == None
    new_format = re.sub('\D','',str(value))
    new_format = float(new_format) / 100 if not is_int else int(new_format)
    return "R$ {:.2f}".format(new_format).replace('.',',')


import re
text = """
Hello, you can contact John at john.doe@example.com for sales inquiries.
For support, reach out to Jane at jane_doe123@service.net.
Additionally, our HR department can be contacted via hr@company.org.
"""
def email_finder(text):
    pattern = r"\w+[\w.%+-]*@\w+\.\w{2,3}"
    matches = re.findall(pattern,text)
    return matches

emails_list = email_finder(text)
for email in emails_list:
    print(f"{email} found at {text.find(email)}")
    
    
def encrypt_data(text,c=0):
    pattern =  r"\w+[\w.%+-]*@\w+\.\w{2,3}"
    res=re.sub(pattern,'***********',text,count=c)
    return res

new_text = encrypt_data(text)
print(new_text)
print('-'*50)
new_text = encrypt_data(text,1)
print(new_text)
print('-'*50)
new_text = encrypt_data(text,2)
print(new_text)
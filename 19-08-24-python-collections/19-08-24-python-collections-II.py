history = ['facebook','instagram','facebook','youtube','linkedin',
           'facebook','linkedin','youtube','linkedin','reddit']

set_history = set(history)#we are removing ducplicates
print(set_history)
list_of_websites = list(set_history)
for website in list_of_websites:
    print(f'user has visited {website}')
    

from collections import Counter  
website_count = Counter(history)   
print(website_count)
user_permissions = {
    "user1": ["read", "write"],
    "user2": ["read"],
    "user3": ["write"],
}

def authorize(permission):
    def decorator(func):
        def wrapper(user):
            if user in user_permissions and permission in user_permissions[user]:
                return func(user)
            
            else :
                return f"{user} is not authorized to {permission}"
        return wrapper
    return decorator

@authorize('read')
def read_data(username):
    return f"{username} is reading the data"

@authorize('write')
def write_data(username):
    return f"{username} is writing the data"

user1_result_read = read_data("user1")
user1_result_write = write_data("user1")
user2_result_read = read_data("user2")
user2_result_write = write_data("user2")#
user3_result_write = write_data("user3")
user3_result_read = read_data("user3")#
user4_result_read = read_data("killian")#

print(user1_result_read)  
print(user1_result_write)
print('\n')
print(user2_result_read)  
print(user2_result_write)
print('\n')
print(user3_result_write)  
print(user3_result_read)
print('\n')
print(user4_result_read)
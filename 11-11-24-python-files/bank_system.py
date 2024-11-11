import json
from stringcolor import *
import time

def load_clients():
    with open('clients.json') as file:
        data = json.load(file)#We converting the json data into python dict
    return data['clients']


def save_clients(clients):
    with open("clients.json","w") as file:
        json.dump({'clients':clients},file,indent=4)


def add_client(clients,client_name,client_dob,client_balance):
    if clients == []:
        client_id = 1
    else :
        client_id=clients[-1]['client_id'] +1 

    client_data = {
        "client_id":client_id,
        "client_name":client_name,
        "dob":client_dob,
        "balance":client_balance
    }
    clients.append(client_data)
    save_clients(clients)

def get_client(clients,client_id):
    for client in clients:
        if client["client_id"] == client_id:
            return client
    return None

def update_client(clients,client_id,client_name=None,client_dob=None,client_balance=None):
    client=get_client(clients,client_id)
    if client:
        if client_name:
            client['client_name']=client_name
        if client_dob:
            client['dob']=client_dob
        if client_balance:
            client['balance'] = client_balance
        save_clients(clients)
    else:
        print(cs("we dont have this client","red"))

def remove_client(clients: list, client_id):
    for id, client in enumerate(clients):
        if client["client_id"] == client_id:
            clients.pop(id)
            break
    save_clients(clients)

def remove_client_1(clients,client_id):
    client = get_client(clients,client_id)
    clients.remove(client)
    save_clients(clients)

def display_client(clients,client_id):
    client = get_client(clients,client_id)
    print(cs(f"Client name {client['client_name']}",'blue'))
    print(cs(f"Client dob {client['dob']}",'green'))
    print(cs(f"Client balance {client['balance']}",'orchid'))

def clients_overview(clients):
    for client in clients:
        print(cs(f"Client id {client['client_id']}",'red'))
        print(cs(f"Client name {client['client_name']}",'blue'))
        print(cs(f"Client dob {client['dob']}",'green'))
        print(cs(underline(f"Client balance {client['balance']}"),'orchid'))
        print(cs('-'*50,'yellow'))
        time.sleep(1.5)

def get_total_amount(clients):
    total = sum([client['balance'] for client in clients])   
    return total



def transfer_money(clients,from_client,to_client,amount):
    pass

clients = load_clients()
#add_client(clients,'Nizar','01/01/2000',1000)
#add_client(clients,'Lisa','01/01/2000',100000000)
# # add_client(clients,'Diego','01/01/2000',100000000)
# client_1 = get_client(clients,1)
# print(client_1)
#update_client(clients,2,client_balance=5200000)
#update_client(clients,3,client_name="Juan Diego",client_dob="02/02/2002")
#remove_client_1(clients,2)
#display_client(clients,3)
clients_overview(clients)
print(get_total_amount(clients))


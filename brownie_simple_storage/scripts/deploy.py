# from brownie import accounts, config, SimpleStorage, network
# # import os

# def get_account():
#         if network.show_active() == "development":
#             return accounts[0]
#         else:
#             return accounts.add(config["wallets"]["from_key"])
# def deploy_simple_storage():
#     account = get_account()
#     simple_storage = SimpleStorage.deploy({"from": account})
#     stored_value = simple_storage.retrieve()
#     print(stored_value)
#     transaction = simple_storage.store(15, {"from": account})
#     transaction.wait(1)
#     updated_stored_value = simple_storage.retrieve()
#     print(updated_stored_value)
#     # # print(account)

#     # # method3
#     # account = accounts.add(config["wallets"]["from_key"])
#     # print(account)



# def main():
#     deploy_simple_storage()
from brownie import accounts, config, SimpleStorage, network

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def main():
    deploy_simple_storage()

import os
from brownie import TestSwapFactory, accounts

def main():
    test_account = accounts.add(os.getenv("PRIVATE_KEY"))
    token = TestSwapFactory.deploy(test_account, {'from': test_account})
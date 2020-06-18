import pandas as pd

ENVIRONMENT= "dev"


def real_data():
    print("return real data")


def data_for_test():
    print("return test fake data")
    return "test"

fetch_data = real_data if ENVIRONMENT == "prod" else data_for_test

data = fetch_data()

print(data)


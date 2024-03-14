from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import ListAccountsRequest
from alpaca.broker.enums import AccountEntities

def api-key = "PK9L065RFKJRM29F1UK2"
def secret-key = "qwaGuecU2Y4csUpIagvhzebK19eXClvLfJvhlT1a"
def base-url = "https://paper-api.alpaca.markets/v2"

broker_client = BrokerClient('api-key', 'secret-key', 'base-url')

# search for accounts created after January 30th 2022.
# Response should contain Contact and Identity fields for each account.
filter = ListAccountsRequest(
                    created_after=datetime.datetime.strptime("2022-01-30", "%Y-%m-%d"),
                    entities=[AccountEntities.CONTACT, AccountEntities.IDENTITY]
                    )

accounts = broker_client.list_accounts(search_parameters=filter)
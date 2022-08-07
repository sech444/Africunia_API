from random import seed
from ripple_api import RippleDataAPIClient
from pprint import pprint

api = RippleDataAPIClient('https://data.ripple.com')
# to get name of a specific transaction type please refer to this link:
# https://developers.ripple.com/transaction-types.html
query_params = dict(type="Payment")
txs = api.get_transactions(**query_params)
#pprint(txs)


acct_info = api(
    account="rBtXmAdEYcno9LWRnAGfT9qBxCeDvuVRZo",
    ledger_index="current",
    queue=True,
    strict=True,
)
response = api.request(acct_info)
result = response.result
import json
print(json.dumps(result["account_data"], indent=4, sort_keys=True))
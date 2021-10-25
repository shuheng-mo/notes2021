import json
from urllib import request

import msal

PERMISSIONS = ["Calendars.Read"]

def do_ms_login():
    cache = msal.SerializableTokenCache()
    app = msal.PublicClientApplication(
        "b1efbb2e-a265-41d2-a42b-7f49fd25dec0",
        authority="https://login.microsoftonline.com/2b897507-ee8c-4575-830b-4f8267c3d307",
        token_cache=cache
        )

    result = None
    accounts = app.get_accounts()
    if accounts:
        chosen = accounts[0]
        result = app.acquire_token_silent(PERMISSIONS, account=chosen)
    if not result:
        flow = app.initiate_device_flow(scopes=PERMISSIONS)
        print(flow["message"])
        result = app.acquire_token_by_device_flow(flow)

    try:
        token = result['access_token']
    except KeyError:
        print("No token issued. If deleting token_cache.bin and retrying doesn't work, please check for an update")
        sys.exit(1)

    return token

token = do_ms_login()

req = request.Request("https://graph.microsoft.com/v1.0/me/calendar/events",
                      method="GET", data={})

req.add_header('content-type', 'application/json')
req.add_header('Host', "graph.microsoft.com")
req.add_header('Authorization', f'Bearer {token}')

resp = request.urlopen(req)

print(json.load(resp)[:5])
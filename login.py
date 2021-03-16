def login(email, password):
    import requests
    import json
    import configparser
    from halo import Halo
    # input
    email = email
    password = password
    # config
    config = configparser.ConfigParser()
    CONFIG_FILE = 'fetch.cfg'
    config.read(CONFIG_FILE)
    url = config.get('DEFAULT', 'url')
    headers = {'Content-Type': 'application/json'}
    tokenAuth = """mutation {
      tokenAuth(
          email: "%s"
          password: "%s"
      ) {
          token
          success
          errors
      }
    }"""%(email, password)
    # login
    # with Halo(text='Logining', spinner='dots'):
    try:
        r = requests.post(url, json={'query': tokenAuth}, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        print('An network error occurred.', e)
    else:
        queryResults = json.loads(r.text)
        success = queryResults["data"]["tokenAuth"]["success"]
        if success == False:
            # INVALID_CREDENTIALS
            # NOT_VERIFIED
            # NEED_MANUAL_VERIFICATION
            ErrMessage = queryResults["data"]["tokenAuth"]["errors"]["nonFieldErrors"][0]["message"]
            print(f'\n{ErrMessage}')
            return
        else:
            # print(f'\nLogin successfully.')
            JWT = queryResults["data"]["tokenAuth"]["token"]
            return JWT

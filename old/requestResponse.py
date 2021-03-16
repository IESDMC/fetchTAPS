def requestResponse(format, tb, te, proj, net, sta, loc, cha, label, JWT):
    import requests
    import json
    import configparser
    from halo import Halo
    # input
    format = format
    tb = tb
    te = te
    proj = proj
    net = net
    sta = sta
    loc = loc
    cha = cha
    label = label
    JWT = JWT
    # config
    config = configparser.ConfigParser()
    CONFIG_FILE = 'fetch.cfg'
    config.read(CONFIG_FILE)
    url = config.get('DEFAULT', 'url')
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT ' + JWT}
    responseRequestMutation = """mutation {
        responseRequestMutation(
            format: "%s",
            tb: "%s",
            te: "%s",
            proj: "%s",
            net: "%s",
            sta: "%s",
            loc: "%s",
            cha: "%s",
            label: "%s",
        ) {
            success
            format
            tb
            te
            proj
            net
            sta
            loc
            cha
            label
            statusCode
            text
            downloadUrl
        }
    }"""%(format, tb, te, proj, net, sta, loc, cha, label)
    # print(responseRequestMutation)
    # request
    with Halo(text='Processing', spinner='dots'):
        try:
            r = requests.post(url, json={'query': responseRequestMutation}, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
            print('An network error occurred.', e)
        else:
            queryResults = json.loads(r.text)
            # print(queryResults)
            success = queryResults["data"]["responseRequestMutation"]["success"]
            if success == False:
              ErrMessage = queryResults["data"]["responseRequestMutation"]["errors"]["nonFieldErrors"][0]["message"]
              print(f'\n{ErrMessage}')
              return
            else:
              statusCode = queryResults["data"]["responseRequestMutation"]["statusCode"]
              if statusCode == 404:
                # NO DATA AVAILABLE
                ErrMessage = queryResults["data"]["responseRequestMutation"]["text"]
                print(f'\n{ErrMessage}')
                return
              elif statusCode == 200:
                # SUCCESS
                downloadUrl = queryResults["data"]["responseRequestMutation"]["downloadUrl"]
                print(f'\n{downloadUrl}')
                return downloadUrl
              else:
                # ERROR
                ErrMessage = ('An network error occurred.')
                print(f'\n{ErrMessage}')

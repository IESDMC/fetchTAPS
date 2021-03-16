def requestPlot(tb, te, proj, net, sta, loc, cha, JWT):
    import requests
    import json
    import configparser
    from halo import Halo
    # input
    tb = tb
    te = te
    proj = proj
    net = net
    sta = sta
    loc = loc
    cha = cha
    JWT = JWT
    # config
    config = configparser.ConfigParser()
    CONFIG_FILE = 'fetch.cfg'
    config.read(CONFIG_FILE)
    url = config.get('DEFAULT', 'url')
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT ' + JWT}
    plotRequestMutation = """mutation {
        plotRequestMutation(
            tb: "%s",
            te: "%s",
            proj: "%s",
            net: "%s",
            sta: "%s",
            loc: "%s",
            cha: "%s",
        ) {
            success
            tb
            te
            proj
            net
            sta
            loc
            cha
            statusCode
            text
            downloadUrl
        }
    }"""%(tb, te, proj, net, sta, loc, cha)
    # print(plotRequestMutation)
    # request
    with Halo(text='Processing', spinner='dots'):
        try:
            r = requests.post(url, json={'query': plotRequestMutation}, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
            print('An network error occurred.', e)
        else:
            queryResults = json.loads(r.text)
            # print(queryResults)
            success = queryResults["data"]["plotRequestMutation"]["success"]
            if success == False:
              ErrMessage = queryResults["data"]["plotRequestMutation"]["errors"]["nonFieldErrors"][0]["message"]
              print(f'\n{ErrMessage}')
              return
            else:
              statusCode = queryResults["data"]["plotRequestMutation"]["statusCode"]
              if statusCode == 404:
                # NO DATA AVAILABLE
                ErrMessage = queryResults["data"]["plotRequestMutation"]["text"]
                print(f'\n{ErrMessage}')
                return
              elif statusCode == 200:
                # SUCCESS
                downloadUrl = queryResults["data"]["plotRequestMutation"]["downloadUrl"]
                print(f'\n{downloadUrl}')
                return downloadUrl
              else:
                # ERROR
                ErrMessage = ('An network error occurred.')
                print(f'\n{ErrMessage}')

def requestAsyncPlot(tb, te, proj, net, sta, loc, cha, JWT):
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
    asyncPlotRequestMutation = """mutation {
        asyncPlotRequestMutation(
            tb: "%s",
            te: "%s",
            proj: "%s",
            net: "%s",
            sta: "%s",
            loc: "%s",
            cha: "%s",
        ) {
            success
            text
            orderId
        }
    }"""%(tb, te, proj, net, sta, loc, cha)
    # print(asyncPlotRequestMutation)
    # request
    with Halo(text='Processing', spinner='dots'):
        try:
            r = requests.post(url, json={'query': asyncPlotRequestMutation}, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
            print('An network error occurred.', e)
        else:
            queryResults = json.loads(r.text)
#            print(queryResults)
            success = queryResults["data"]["asyncPlotRequestMutation"]["success"]
            if success == False:
                text = queryResults["data"]["asyncPlotRequestMutation"]["text"]
                print(f'\n{text}')
                res = {
                    'success': success,
                    'text': text
                }
                return res
            else:
                text = queryResults["data"]["asyncPlotRequestMutation"]["text"]
                orderId = queryResults["data"]["asyncPlotRequestMutation"]["orderId"]
                print(f'\n{text}\norderId: {orderId}')
                res = {
                    'success': success,
                    'text': text,
                    'orderId': orderId
                }
                return res

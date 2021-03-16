def requestAsyncWaveform(outputFormat, tb, te, proj, net, sta, loc, cha, label, JWT):
    import requests
    import json
    import configparser
    from halo import Halo
    # input
    outputFormat = outputFormat
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
    asyncWaveformRequestMutation = """mutation {
        asyncWaveformRequestMutation(
            outputFormat: "%s",
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
            text
            orderId
        }
    }"""%(outputFormat, tb, te, proj, net, sta, loc, cha, label)
    # print(asyncWaveformRequestMutation)
    # request
    with Halo(text='Processing', spinner='dots'):
        try:
            r = requests.post(url, json={'query': asyncWaveformRequestMutation}, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
            print('An network error occurred.', e)
        else:
            queryResults = json.loads(r.text)
            success = queryResults["data"]["asyncWaveformRequestMutation"]["success"]
            if success == False:
                text = queryResults["data"]["asyncWaveformRequestMutation"]["text"]
                print(f'\n{text}')
                res = {
                    'success': success,
                    'text': text
                }
                return res
            else:
                text = queryResults["data"]["asyncWaveformRequestMutation"]["text"]
                orderId = queryResults["data"]["asyncWaveformRequestMutation"]["orderId"]
                print(f'\n{text}\norderID: {orderId}')
                res = {
                    'success': success,
                    'text': text,
                    'orderId': orderId
                }
                return res

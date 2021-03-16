def getOrderStatus(email, password, orderId):
    import requests
    import json
    import configparser
    import time
    from halo import Halo
    from login import login
    # input
    email = email
    password = password
    orderId = orderId

    # config
    config = configparser.ConfigParser()
    CONFIG_FILE = 'fetch.cfg'
    config.read(CONFIG_FILE)
    url = config.get('DEFAULT', 'url')
    JWT = ''
    headers = {'Content-Type': 'application/json', 'Authorization': 'JWT ' + JWT}
    orderStatus = """query{
        orderStatus(
            orderId:"%s"
        ) {
        status
        log
        url
    }
    }"""%(orderId)
    # print(orderStatus)
    # request
    spinner = Halo(text='Queue', spinner='dots')
    spinner.start()
    # Run time consuming work here
    # You can also change properties for spinner as and when you want
    # with Halo(text='Processing', spinner='dots'):
    status = ''
    while (True):
        try:
            # print(f'headers: {headers}')
            r = requests.post(url, json={'query': orderStatus}, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
            print('An network error occurred.', e)
        else:
            queryResults = json.loads(r.text)
            status = queryResults["data"]["orderStatus"]["status"]
            if status == 'Invalid token':
                JWT = login(email, password)
                # print(f'JWT: {JWT}')
                if JWT == None:
                    return
                headers = {'Content-Type': 'application/json', 'Authorization': 'JWT ' + JWT}
            elif status == 'Queue':
                spinner.text = status
                log = queryResults["data"]["orderStatus"]["log"]
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log
                }
            elif status == 'Success':
                spinner.text = status
                log = queryResults["data"]["orderStatus"]["log"]
                url = queryResults["data"]["orderStatus"]["url"]
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log,
                    'url': url
                }
                print(f'\n{status}')
                break
            elif status == 'Error':
                spinner.text = status
                print(f'\n{status}')
                log = queryResults["data"]["orderStatus"]["log"]
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log,
                }
                break
            elif status == 'Expired':
                spinner.text = status
                print(f'\n{status}')
                log = queryResults["data"]["orderStatus"]["log"]
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log,
                }
                break
            elif status == 'Working':
                spinner.text = status
                log = queryResults["data"]["orderStatus"]["log"]
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log,
                }
            else:
                log = queryResults["data"]["orderStatus"]["log"]
                print(f'\n{status}')
                # print(f'\n{log}')
                res = {
                    'status': status,
                    'log': log,
                }
                break
            time.sleep(5)
    spinner.stop()
    return res
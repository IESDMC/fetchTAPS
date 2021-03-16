def fetchWaveform(args):
    # input
    email = args.u[0]
    password = args.p[0]
    format = args.format[0]
    tb = args.tb[0]
    te = args.te[0]
    proj = args.proj[0]
    net = args.net[0]
    sta = args.sta[0]
    loc = args.loc[0]
    cha = args.cha[0]
    label = args.label[0]
    from login import login
    from requestAsyncWaveform import requestAsyncWaveform
    from getOrderStatus import getOrderStatus
    from download import download
    
    # login
    JWT = login(email, password)
    if JWT == None:
        return

    # request
    res = requestAsyncWaveform(format, tb, te, proj, net, sta, loc, cha, label, JWT)
    if res['success'] == False:
        return
    else:
        orderId = res['orderId']

    # check order
    #res = getOrderStatus(email, password, orderId)
    #if res['status'] == 'Error':
    #    return
    #else:
    #    url = res['url']
        
    # fetch
    #download(url)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='fetchWaveform',
    epilog='Example: python fetchWaveform.py -u chute@earth.sinica.edu.tw -p 27839910#2705 -format mseed -tb 2008-02-17T20:31:00 -te 2008-02-17T20:41:00 -proj 2008NSN,2008NSS -net TW -sta all -loc all -cha HHZ -label 20080217203100')
    parser.add_argument('-format', metavar='format', type=str, nargs='+',
                        help='-format mseed', dest='format', required=True)
    parser.add_argument('-tb', metavar='time begin', type=str, nargs='+',
                        help='-tb 2008-02-17T20:31:00', dest='tb', required=True)
    parser.add_argument('-te', metavar='time end', type=str, nargs='+',
                        help='-te 2008-02-17T20:41:00', dest='te', required=True)
    parser.add_argument('-proj', metavar='project', type=str, nargs='+',
                        help='-proj 2008NSN,2008NSS', dest='proj', required=True)
    parser.add_argument('-net', metavar='network', type=str, nargs='+',
                        help='-net TW', dest='net', required=True)
    parser.add_argument('-sta', metavar='station', type=str, nargs='+',
                        help='-sta all', dest='sta', required=True)
    parser.add_argument('-loc', metavar='location', type=str, nargs='+',
                        help='-loc all', dest='loc', required=True)
    parser.add_argument('-cha', metavar='channel', type=str, nargs='+',
                        help='-cha HHZ', dest='cha', required=True)
    parser.add_argument('-label', metavar='label', type=str, nargs='+',
                        help='-label 20080217203100', dest='label', required=True)
    parser.add_argument('-u', metavar='email', type=str, nargs='+',
                        help='-u chute@earth.sinica.edu.tw', dest='u', required=True)
    parser.add_argument('-p', metavar='password', type=str, nargs='+',
                        help='-p 27839910#2705', dest='p', required=True)
    args = parser.parse_args()
    fetchWaveform(args)

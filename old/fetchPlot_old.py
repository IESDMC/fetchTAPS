def fetchPlot(args):
    # input
    email = args.u[0]
    password = args.p[0]
    tb = args.tb[0]
    te = args.te[0]
    proj = args.proj[0]
    net = args.net[0]
    sta = args.sta[0]
    loc = args.loc[0]
    cha = args.cha[0]
    if sta == 'all':
        sta = '*'
    if loc == 'all':
        loc = '*'
    # login
    from login import login
    JWT = login(email, password)
    if JWT == None:
        return
    # request
    from requestPlot import requestPlot
    url = requestPlot(tb, te, proj, net, sta, loc, cha, JWT)
    if url == None:
        return
    # check order
        # developing
    # fetch
    # import webbrowser
    # webbrowser.open(url)
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='fetchPlot',
    epilog='Example: python fetchPlot.py -u chute@earth.sinica.edu.tw -p 27839910#2705 -tb 2008-02-17T20:31:00 -te 2008-02-17T20:41:00 -proj 2008NSN,2008NSS -net TW -sta NSN07 -loc all -cha HHZ')
    parser.add_argument('-tb', metavar='time begin', type=str, nargs='+',
                        help='-tb 2008-02-25T08:08:32', dest='tb', required=True)
    parser.add_argument('-te', metavar='time end', type=str, nargs='+',
                        help='-te 2008-02-25T08:11:32', dest='te', required=True)
    parser.add_argument('-proj', metavar='project', type=str, nargs='+',
                        help='-proj 2008NSN', dest='proj', required=True)
    parser.add_argument('-net', metavar='network', type=str, nargs='+',
                        help='-net TW', dest='net', required=True)
    parser.add_argument('-sta', metavar='station', type=str, nargs='+',
                        help='-sta NSN07', dest='sta', required=True)
    parser.add_argument('-loc', metavar='location', type=str, nargs='+',
                        help='-loc all', dest='loc', required=True)
    parser.add_argument('-cha', metavar='channel', type=str, nargs='+',
                        help='-cha HHZ', dest='cha', required=True)
    parser.add_argument('-u', metavar='email', type=str, nargs='+',
                        help='-u chute@earth.sinica.edu.tw', dest='u', required=True)
    parser.add_argument('-p', metavar='password', type=str, nargs='+',
                        help='-p 27839910#2705', dest='p', required=True)
    args = parser.parse_args()
    fetchPlot(args)
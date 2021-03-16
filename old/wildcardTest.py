def wildcardTest(args):
    cha = args.cha[0]
    print(cha)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='wildcardTest',
    epilog='Example: python wildcardTest.py -cha \'HH?\'')
    parser.add_argument('-cha', metavar='-cha \'HH?\'', type=str, nargs='+',
                        help='channel name. e.g. HHZ,HHN,HHE,BH?...', required=True)
    args = parser.parse_args()
    wildcardTest(args)
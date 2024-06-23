import argparse
import os

def main():
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__), usage='%(prog)s [options]')

    parser.add_argument('name', help="the name of the note")
    parser.add_argument('-f', '--folder', metavar="PATH", help='The folder the note is stored within')
    parser.add_argument('-T', '--tag', metavar='TAG:TAG', help='Colon seperated tags associated with the note')
    parser.add_argument('--findTag', metavar="TAG:TAG", help='locates any notes with specific tags')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()

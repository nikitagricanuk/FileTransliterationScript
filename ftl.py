from transliterate import translit
import argparse
import os 

parser = argparse.ArgumentParser(description='Script for file names transliteration')

parser.add_argument('filenames', type=str, nargs='*', metavar='Filename', 
                    help='Files to transliterate')

parser.add_argument('--english', type=bool, metavar='LANG', default=True,
                    help='Trasliterate to English, default is True')

parser.add_argument('--lang', type=str, metavar='LANG', required=True,
                    help='Target language')

args = parser.parse_args()

for filename in args.filenames:
    if os.path.exists(filename):
        new_filename = translit(filename, args.lang, reversed=args.english)
        os.rename(filename, new_filename)
    else:
        print("File {filename} not found.")
# -*- coding: utf-8 -*-
from cls_mkparser import markdownParser
from cls_interface import interface
import sys
import getopt

def main(argv):
    # Erstelle Parserobjekt
    parser = markdownParser()

    # Wenn Parameter an das Programm übergeben wurden
    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(argv, "f:")

            # War das Argument "-f"
            for opt, arg in opts:
                if opt == '-f':
                    filename = arg
                    parsed = parser.analysiereDatei(filename)
                    datei = open("auto_parsed.html","w")
                    datei.write(parsed)
                # Wenn nicht -> Fehlermeldung
                else:
                    print "Usage: \n " \
                          "\t main.py \t Opens the normal GUI \n" \
                          "\t main.py -f filename \t Parses the file and save the result to auto_parsed.html"
        except Exception as e:
            print "Usage: \n " \
                  "\t main.py \t Opens the normal GUI \n" \
                  "\t main.py -f filename \t Parses the file and save the result to auto_parsed.html"
    else:
        inter = interface()

if __name__ == "__main__":
    main(sys.argv[1:])
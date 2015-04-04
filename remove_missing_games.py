#!/usr/local/bin/python
from xml.etree import ElementTree
import sys, getopt
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"i:o:m:",["ifile=","ofile=","missinggames="])
    except getopt.GetoptError:
      print 'remove_missing_games.py -i <inputfile> -o <outputfile> -m <missinggamelist>'
      sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputXml= arg
        elif opt in ("-o", "--ofile"):
            outputXml = arg
        elif opt in ("-m", "--missinggames"):
            missing_games = arg

    tree = ElementTree.parse(inputXml)   

    root=tree.getroot()
    with open(missing_games) as f:
        lines = f.read().splitlines()


    for child in root:
        if child.attrib['name'] in lines:
            print child.attrib['name']
            root.remove(child)
    tree.write(outputXml)
if __name__ == "__main__":
    main(sys.argv[1:])
    

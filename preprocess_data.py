from os import listdir
from xml.etree import ElementTree


def extract_boxes(filename):
        # load and parse the file
        tree = ElementTree.parse(filename)
        # get the root of the document
        root = tree.getroot()
        # extract each bounding box
        boxes = list()
        for name in root.findall('.//name'):
            name = name.text.replace(' ', '')
            if name not in ['1', '2', '4', '5']:
                print(filename)
                print('"', name, '"')


annots_dir = './dataset/annots/'
annots_names = listdir(annots_dir)

for annot_name in annots_names:
    extract_boxes(annots_dir + annot_name)

from os import listdir
from xml.etree import ElementTree


def merge_4_types(filename):
    # load and parse the file
    tree = ElementTree.parse(filename)
    # get the root of the document
    root = tree.getroot()
    # extract each bounding box
    boxes = list()
    for name in root.findall('.//name'):
        if name.text == '4a' or name.text == '4b' or name.text == '4c':
            name.text = '4'
    
    # save xml  file
    tree.write(filename)


def remove_spaces(filename):
    # load and parse the file
    tree = ElementTree.parse(filename)
    # get the root of the document
    root = tree.getroot()
    # extract each bounding box
    boxes = list()
    for name in root.findall('.//name'):
        if name.text not in ['1', '2', '4', '5']:
            print(f'"{name.text}"')
            new_name = name.text.replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '')
            print(filename)
            print(f'"{new_name}"')
            name.text = new_name
    
    # save xml file
    tree.write(filename)


annots_dir = './dataset/annots/'
annots_names = listdir(annots_dir)

for annot_name in annots_names:
    remove_spaces(annots_dir + annot_name)
    merge_4_types(annots_dir + annot_name)

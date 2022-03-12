import os


images_dir = './dataset/images/'
annots_dir = './dataset/annots/'
image_names = os.listdir(images_dir)

for i, image_name in enumerate(image_names):
    file_extension = image_name[-4:]
    file_name = image_name[:-4]
    image_name = images_dir + file_name + file_extension
    new_image_name = images_dir + str(i) + file_extension
    annot_name = annots_dir + file_name + '.xml'
    new_annot_name = annots_dir + str(i) + '.xml'
    # rename image
    os.rename(image_name, new_image_name)
    os.rename(annot_name, new_annot_name)
    print(image_name, annot_name)

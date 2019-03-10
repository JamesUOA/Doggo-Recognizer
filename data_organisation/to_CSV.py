import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def to_csv(path):
    """
    function to merge datafiles into a single csv
    :param path: path to the file locations
    :return: combined csv
    """
    xml_list = []
    for xml_file in glob.glob(path + '/*'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for file in glob.glob('Annotation/*'):
        print(file)
        name = file.split("\\")[1]
        training_image_path = os.path.join(os.getcwd(), file)
        training_xml_df = to_csv(training_image_path)
        training_xml_df.to_csv('data/' + name + '.csv', index=None)

    print('Successfully converted to csv.')


main()

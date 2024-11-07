import xml.etree.ElementTree as ET
import logging

# Third task - parsing in xml file

def find_incoming_value_by_group_number(group_number):

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:

        tree = ET.parse('./ideas_for_test/work_with_xml/groups.xml')
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')

            if number is not None and int(number.text) == group_number:
                timing_exbytes = group.find('timingExbytes')

                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')

                    if incoming is not None:
                        logging.info(f"Group {group_number} 'incoming' value: {incoming.text}")
                        return


        logging.info(f"Group {group_number} not found or does not contain 'timingExbytes/incoming'.")

    except ET.ParseError as e:
        logging.error(f"Failed to parse XML file './ideas_for_test/work_with_xml/groups.xml': {e}")


if __name__ == '__main__':
    group_number = 1
    find_incoming_value_by_group_number(group_number)
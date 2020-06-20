import xml.etree.ElementTree as ET


def parse_port_protocol(nmap_file):
    """define function parse_port_protocol that will read and parse the xml file"""

    # use parse() to parse the xml file
    nmap_xml = ET.parse(nmap_file)
    # start with finding the root
    root = nmap_xml.getroot()
    # create empty dictionary dictionary_address_ip_and_ports
    dictionary_address_ip_and_ports = {}
    # find host inside the xml file first
    for host in root.iter("host"):
        # then locate address inside the host
        for address in host.iter("address"):
            # create empty dictionary dictionary_portid_and_protocol
            dictionary_portid_and_protocol = {}
            # finally locate the portid inside the host
            for ports in host.iter("port"):
                # store portid and protocol into dictionary_portid_and_protocol
                dictionary_portid_and_protocol[ports.get("portid")] = ports.get("protocol")
            # store dictionary_portid_and_protocol into dictionary_address_ip_and_ports
            dictionary_address_ip_and_ports[address.get("addr")] = dictionary_portid_and_protocol
    # return dictionary_store_ip_and_ports
    return dictionary_address_ip_and_ports


def display_port_protocol(dictionary_address_ip_and_ports):
    """define a function display_port_protocol that will print ip: [list_ports]"""

    # use items() method to present the ports in ip address that we stored in the dictionary
    for address, ip_and_ports in dictionary_address_ip_and_ports.items():
        print(address, ":", ip_and_ports)


def main():
    """define main function"""

    # store filename that we want to check in file_to_parse
    file_to_parse = "f_router.xml"
    # store the return dictionary from file_to_purse in dictionary_ip_and_ports
    dictionary_address_ip_and_ports = parse_port_protocol(file_to_parse)
    # use function display_port_protocol with input of dictionary_ip_and_ports to display what we are looking for
    display_port_protocol(dictionary_address_ip_and_ports)


if __name__ == "__main__":
    main()
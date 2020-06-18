import xml.dom.minidom
# import the xml.dom.minidom to use purse xml file
import collections
# import collections so we can append an element to a key in dictionary


def file_to_purse():
    """define function file_to_purse that will read and purse the xml file"""

    # use parse() to parse the xml file
    file_to_check = xml.dom.minidom.parse("f_router.xml")
    # find all ports inside the xml file
    ports = file_to_check.getElementsByTagName("port")
    # find all addresses inside the xml file
    addresses = file_to_check.getElementsByTagName("address")
    # create empty dictionary dictionary_to_check that will store the ip address and list_ports
    # use collections.defaultdict() to store multiple elements in one key
    dictionary_to_check = collections.defaultdict(list)
    # use for loop to store ip addresses and port_list into the dictionary_to_check
    for address in addresses:
        for port in ports:
            dictionary_to_check[address.getAttribute("addr")].append(port.getAttribute("portid"))
    # return the dictionary_to_check
    return dictionary_to_check


def display_output(dictionary_to_check):
    """define a function display_output that print ip: [list_ports] """

    # use items() method to present the ports in ip address that we stored in the dictionary
    for ip, ports in dictionary_to_check.items():
        print(ip, ":", ports)


def main():
    """define main function"""

    # store the return dictionary from file_to_purse in dictionary_to_check
    dictionary_to_check = file_to_purse()
    # use display_output function to present ip address : [list_ports]
    display_output(dictionary_to_check)


if __name__ == "__main__":
    main()
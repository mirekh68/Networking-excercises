import sys

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import re

#ipstr = string of the form nnnn.nnnn.nnnn.nnnn
#returns 4-tuple of ip4 numbers in interval [0,256) 
def parse_ip(ipstr):
    v4 = ipstr.split('.')
    if len(v4) != 4:
        raise Exception(f"Bad format of ip address: {ipstr}")
    for i in range(0,4):
        oct = int(v4[i])
        if oct < 0 or oct > 255:
            raise Exception(f"One of the octet has forbidden value: {oct}")
        v4[i] = oct

    return tuple(v4)
    
def get_octet_mask(mask):
    mask0 = [255, 255, 255, 255]
    if type(mask) is int:
        dmask8 = mask//8
        rmask8 = mask%8
        for i in range(1,dmask8):
            mask0[-i] = 0

        mask0[-dmask8] &= 255 >> (8-rmask8)
        return tuple(mask0)
    elif type(mask) is str:
        return parse_ip(mask)
    else:
        raise Exception(f"Unexpected type of mask : {mask} type: {type(mask)}")




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sys.version_info)
    print(sys.exc_info())
    print(sys.executable)
    print(sys.platform)
    print(get_octet_mask(8))
    print(get_octet_mask(16))
    print(get_octet_mask(32))
    print(get_octet_mask(10))
    print(get_octet_mask(4))
    print(get_octet_mask(26))
    print(get_octet_mask("255.255.128.0"))

    #print(parse_ip('111.222.33.0'))
    #print(parse_ip('111.a.33.0.x'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

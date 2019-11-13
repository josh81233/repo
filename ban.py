MRS_ORDER = [
    'R', 'M', 'M1'
]

MRC_ORDER = [
    'coproc', 'opc1', 'CRn', 'CRm', 'opc2'
]

MCRR_ORDER = [
    'coproc', 'CRm', 'opc1'
]

VMRS_ORDER = [
    'reg'
]

A64_ORDER = [
    "op0", "op1", "CRn", "CRm", "op2", "Rt"
]

ORDER = {('MSR', 'MRS', 'MSRregister'): MRS_ORDER, ('MCR', 'MRC'): MRC_ORDER, ('VMRS', 'VMSR'): VMRS_ORDER, 'SysOpregister': A64_ORDER}

def validate_encoding_order():
    """
    validate the order of encoding in registers

    Args:

    Returns:
        bool: True if valid, False otherwise
    """
    acc = input()
    is_valid = False
    for types, orde in ORDER.items():
        if acc in types:
            key = list(encodings.keys())
            if orde == key:
                is_valid = True
            else:
                is_valid = False
    return is_valid



if __name__ == "__main__":
    encodings = {'R':0b0001,'M':0b1010,'M1':0b1010}
    print(validate_encoding_order())


def xor(a, b):
    result = []
 
    # Skip the first bit, it is always zero
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
 
# Performs Modulo-2 division
def mod2div(dividend, divisor):
 
    pick = len(divisor)
 
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else: 
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
        pick += 1
 
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword

def crc_encode(Mx, Cx):
    pad_len = len(Cx) - 1
    Tx = Mx + '0' * pad_len
    
    remainder = mod2div(Tx, Cx)
    codeword = Mx + remainder
    
    print(f"Data: {Mx} \nEncoding: {Cx} \nRemainder: {remainder} \nCodeword: {codeword}")
    return codeword
    
def crc_check(Px, Cx):
    pad_len = len(Cx) - 1
    
    Mx = Px[:-(pad_len)]
    
    Tx = Mx + '0' * pad_len
    
    remainder = mod2div(Tx, Cx)
    if remainder == Px[-(pad_len):]:
        print("No error detected")
    else:
        print("Error detected")

def main():
    Mx = '10010101110110010101010100011111011010101010111101101101'
    encoding_types = {"parity": '11',
                      "old_mobild_network": '1011',
                      "usb_token": '100101',
                      "bluetooth": '110100111',
                      "ethernet": '100000100110000010001110110110111'}
    for key in encoding_types.keys():
        Cx = encoding_types[key]
        print("-------------------")
        print(f"Encoding type: {key}")
        Px = crc_encode(Mx, Cx)
        
        print("------Checking-------")
        crc_check(Px, Cx)        
        print("-------------------\n")
        
    
if __name__ == '__main__':
    main()
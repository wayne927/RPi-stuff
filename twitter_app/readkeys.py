import struct

def readKeys (filename) :
    filein = open(filename, 'rb')
    
    strings = [ "", "", "", "" ]
    
    for s in xrange(len(strings)) :
        while True :
            ch_int = struct.unpack("i", filein.read(4))[0]
        
            if not ch_int :
                break
        
            ch = chr(ch_int)
        
            if ch == '\n' :
                break
    
            strings[s] = strings[s] + ch

    return strings

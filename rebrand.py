import os
import sys

def main():
    try:
        with open('oeminfo.img', 'rb') as f:
            b = bytearray(f.read())
        m = bytearray(sys.argv[1])
        while len(m) < 127:
            m += '\x00'
        b[369152:369279] = m
        b[393236] = len(sys.argv[1])
        m = bytearray(sys.argv[1])
        while len(m) < 127:
            m += '\xff'

        b[393728:393855] = m
        b[69652] = len(sys.argv[2])
        m = bytearray(sys.argv[2])
        while len(m) < 127:
            m += '\xff'

        b[70144:70271] = m
        franges = ((28672, 32767), (421888, 438271), (33583104, 33587199), (33980416, 33992703))
        for st, en in franges:
            for x in range(st, en + 1):
                b[x] = 255

        with open('output.img', 'wb') as f:
            f.write(b)
        return True
    except:
        return False

if __name__ == '__main__':
    try:
        main()
    except:
        print 'Error'
# The default process of python compression and decompression using bsae64 encoding & zlib
import zlib, sys, base64

def base64_compression():
    text = open('files/small_file.txt', 'r').read()
    print("Raw size: ", sys.getsizeof(text))

    # text.encode() [bytes] is usually good enough, but just wanna do base64 [bytes]
    # compression range is 0-9. 9 is the best and max
    bytes = base64.b64encode(text.encode('utf-8', errors='strict'))
    compressed = zlib.compress(bytes, 9)
    print("Compressed Size with max (9): ", sys.getsizeof(compressed))

    output = open('files/compressed_data.bin', 'wb')
    output.write(compressed)
    output.close()

    decompressed_text = ''
    bytes = open('files/compressed_data.bin', 'rb').read()
    decompressed = zlib.decompress(bytes)
    output = open('files/to_compare.txt', 'w')
    output.write( (base64.b64decode(decompressed)).decode() )
    output.close()
    # compare the file
    to_compare = open('files/to_compare.txt', 'r').read()
    print("Do we get every data back? " , to_compare == text)

if __name__ == '__main__':
    base64_compression()
    print("-----------END--------------")


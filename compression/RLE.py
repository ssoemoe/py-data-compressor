# Run-length encoding (RLE) compression algorithm

def rle_encode(msg):
    encoded = ""
    count = 0
    prev = ""
    for m in msg:
        if count == 0:
            count += 1
            prev = m
        else:
            if m == prev:
                count += 1
                pass
            else:
                encoded += str(count) + prev
                prev = m
                count = 1

    encoded += str(count) + m
    return encoded

def rle_decode(encoded_msg):
    decoded = ""
    for i in range(0, len(encoded_msg), 2):
        decoded += encoded_msg[i + 1] * int(encoded_msg[i])
    return decoded

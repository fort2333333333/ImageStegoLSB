from PIL import Image
from numpy import array
from selection import write, write_opposite, encrypt
import struct

with open("message.txt", "rb") as f:
    MESSAGE = f.read()

MESSAGE = encrypt(MESSAGE)
MESSAGE = struct.pack("<I", len(MESSAGE)) + MESSAGE
MESSAGE_SIZE = len(MESSAGE)

IMAGE = Image.open("raw.png")
IMAGE = array(IMAGE)

Y_SIZE, X_SIZE, _ = IMAGE.shape

def get_bit(bit_index : int) -> int:
    byte_index = bit_index // 8
    if byte_index >= MESSAGE_SIZE:
        return -1
    bit_offset = bit_index % 8
    byte = MESSAGE[byte_index]
    bit = 1 if byte & (0b1 << bit_offset) else 0
    return bit

pos = 0
exit_loop = False
for y in range(Y_SIZE):
    for x in range(X_SIZE):
        if not write(x,y):
            continue
        reverse = write_opposite(x,y)
        for c in (0,1,2):
            b = get_bit(pos)
            if b == -1:
                exit_loop = True
                break
            if reverse:
                b ^= 1
            processed = (IMAGE[y,x,c] & 0b11111110) | b
            IMAGE[y,x,c] = processed
            pos += 1
        if exit_loop: break
    if exit_loop: break

processed_image = Image.fromarray(IMAGE)
processed_image.save("processed.png")

print(f"应写入{MESSAGE_SIZE}字节")
print(f"已写入{pos//8}字节")
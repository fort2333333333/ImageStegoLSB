from PIL import Image
from numpy import array
from selection import write, write_opposite, write_colour, decrypt

IMAGE = Image.open("processed.png")
IMAGE = array(IMAGE)

Y_SIZE, X_SIZE, _ = IMAGE.shape

bits_list = []

for y in range(Y_SIZE):
    for x in range(X_SIZE):
        if not write(x,y):
            continue
        reverse = write_opposite(x,y)
        for c in write_colour(x,y):
            bit = bool(IMAGE[y,x,c] & 0b1)
            if reverse: bit ^= 1
            bits_list.append(bit)

bytes_list = []
message_size = 0
for i in range(0,len(bits_list)>>3<<3,8):
    byte = 0
    for b in range(8):
        if bits_list[i+b]: byte |= 0b1 << b
    if i//8 < 4:
        message_size |= byte << i
    elif i//8 - 4 >= message_size:
        break
    bytes_list.append(byte)

message = bytes(bytes_list[4:])
message = decrypt(message)
with open("message.txt", "wb") as f:
    f.write(message)
print(f"应读取{message_size+4}字节")
print(f"已读取{len(bytes_list)}字节")
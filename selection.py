prime_list = [2]

def exist(target : int) -> bool:
    start = 0
    end = len(prime_list) - 1
    while start <= end:
        mid = (end + start) // 2
        value = prime_list[mid]
        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return True
    return False

def is_prime(num : int):
    if num <= prime_list[-1]:
        if exist(num): return True
        else: return False
    for n in range(prime_list[-1]+1, num+1):
        for prime in prime_list:
            if not n % prime:
                break
        else:
            prime_list.append(n)
    if prime_list[-1] == num: return True
    return False

def write(para1 : int, para2 : int) -> bool:
    return is_prime(para1^para2)

def write_colour(para1 : int, para2 : int) -> tuple[int]:
    if para1 % 3 == 0:
        return (0,)
    if para2 % 3 == 0:
        return (1,)
    return (2,)

def write_opposite(para1 : int, para2 : int) -> bool:
    return False

def encrypt(message : bytes) -> bytes:
    return message

def decrypt(code : bytes) -> bytes:
    return code
def transform_to_dual(dec: int) -> str:
    temp_dec = dec
    if dec == 0:
        return str(0)
    bit: list = []
    while dec:
        bit.append(dec % 2)
        dec >>= 1
    bit = bit[::-1]
    bit = [str(b) for b in bit]
    bit_str: str = "".join(bit)
    assert (bit_str == bin(temp_dec)[2:])

    return bit_str


if __name__ == "__main__":
    print(transform_to_dual(15))

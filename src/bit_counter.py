import functools


class BitCounter:
  DEFAULT_BITMASK_SIZE = 50

  def __init__(self, bitmask_size=DEFAULT_BITMASK_SIZE):
    self.bitmask_size = bitmask_size
    self.bitmask = (0b1 << bitmask_size) - 1

  @functools.cache
  def countSetBits(self, binary_number):
    count = 0
    while (binary_number):
      binary_number &= (binary_number-1)
      count += 1

    return count

  @functools.cache
  def count_set_bits(self, number):
    if number <= 2**self.bitmask_size + 1:
      return self.countSetBits(number)

    extracted_bits = number & self.bitmask
    number = number >> self.bitmask_size

    return self.countSetBits(extracted_bits) + self.count_set_bits(number)

  @functools.cache
  def count_set_bits_loop(self, number):
    bit_count = 0
    while number > 0:
      extracted_bits = number & self.bitmask
      number = number >> self.bitmask_size
      bit_count += self.countSetBits(extracted_bits)
    return bit_count

import unittest
import time

from bit_counter import BitCounter
import random


class TestBitCounterMethods(unittest.TestCase):
  def test_it_exists(self):
    self.assertNotEqual(BitCounter(), None)

  def test_it_counts_bits(self):
    cases = {
        0b10: 1,
        0b11: 2,
        0b100: 1,
        0b10001: 2,
        256: 1,
        2**251: 1,
        3**10: 9,
        0b10: 1,
    }

    for num, bit_count in cases.items():
      self.assertEqual(BitCounter().countSetBits(num),
                       bit_count)
      self.assertEqual(BitCounter().count_set_bits(num), bit_count)
      self.assertEqual(BitCounter().count_set_bits_loop(num), bit_count)

  def test_it_counts_big_bits(self):
    cases = {
        10**20: 26,
        10**12: 13,
        7**19: 31,
        19**7: 18,
        84**96: 217,
        135**99: 359,
    }

    for num, bit_count in cases.items():
      self.assertEqual(BitCounter().countSetBits(num), bit_count)
      self.assertEqual(BitCounter().count_set_bits(num), bit_count)
      self.assertEqual(BitCounter().count_set_bits_loop(num), bit_count)

  def test_it_counts_big_bits_faster(self):
    num_runs = 10
    loop_size = 100
    num = 12**12**4
    duration = 0
    count = 0

    for _ in range(loop_size):
      start = time.perf_counter()
      BitCounter().count_set_bits_loop(num)
      stop = time.perf_counter()
      duration += stop - start
      count += 1
      num += 1

    print(f'On average count big faster took {duration / count} seconds')
    self.assertEqual(None, None)

  # The goal here is to find the optimal mask size given our dictioanry size and the number of times we will sample.
  # What's the optimal $-hit rate we want?
  #

  def test_handles_a_workload(self):
    dictionary_size = 12500
    # sample_count = dictionary_size ** 3
    sample_count = 100_00
    size_options = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    rand_bits = [random.getrandbits(dictionary_size)
                 for _ in range(sample_count)]

    print(f'Sample Size: {sample_count}')
    print(f'Dictionary Size: {dictionary_size}')

    duration = 0
    bit_counter = BitCounter()
    for num in rand_bits:
      num = random.getrandbits(dictionary_size)
      start = time.perf_counter()
      bit_counter.countSetBits(num)
      stop = time.perf_counter()
      duration += stop - start
    print(f'Baseline - Raw bit count: {duration} seconds')
    print(bit_counter.countSetBits.cache_info())
    bit_counter.countSetBits.cache_clear()

    for bitmask_size in size_options:
      print(f'\nBitmask size: {bitmask_size}:')

      duration = 0
      bit_counter = BitCounter(bitmask_size)
      loop_counter = 0
      last_duration_printout = 0
      for num in rand_bits:
        start = time.perf_counter()
        bit_counter.count_set_bits_loop(num)
        stop = time.perf_counter()
        duration += stop - start
        loop_counter += 1
        if loop_counter % (sample_count / 10) == 0:
          print(f'Time for last sample batch: {duration - last_duration_printout}')
          last_duration_printout = duration

      print(f'Loop bit count: {duration} seconds')

      print(bit_counter.countSetBits.cache_info())
      bit_counter.countSetBits.cache_clear()
      print(bit_counter.count_set_bits_loop.cache_info())
      bit_counter.count_set_bits_loop.cache_clear()


if __name__ == '__main__':
  unittest.main()

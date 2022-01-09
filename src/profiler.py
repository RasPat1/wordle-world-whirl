from datetime import datetime
from timer import RepeatTimer


class ProfilerFactory:
  def getProfiler(enabled):
    if enabled:
      return Profiler()
    else:
      return DummyProfiler()


class Profiler:
  _INTERVAL = 5.0
  solution_count = 0
  guess_count = 0
  start_time = None
  stop_time = None
  timer = None
  corpus = None
  cr_score_cache = None
  diff_cache = None
  last_solution_time = None
  solution_times = []
  cache_list = []

  def start(self):
    self.start_time = datetime.now()
    self.last_solution_time = self.start_time
    self._start_timer_thread()

  def stop(self):
    self.stop_time = datetime.now()
    self._stop_timer_thread()

  def get_progress(self):
    return (solution_count, guess_count, start_time)

  def update_progress(self, solution_count, guess_count):
    self.solution_count = solution_count
    self.guess_count = guess_count

  def count_guess(self):
    self.guess_count += 1

  def count_solution(self):
    self.guess_count = 0
    self.solution_count += 1
    elapsed_time_in_seconds = (
        datetime.now() - self.last_solution_time).total_seconds()
    self.solution_times.append(elapsed_time_in_seconds)
    if elapsed_time_in_seconds > self._INTERVAL:
      print(f'Solution {self.solution_count} computed in: {elapsed_time_in_seconds} seconds')
      print(f'Last solution times: {self.solution_times[-5:]}')
    self.last_solution_time = datetime.now()

  def register_corpus(self, corpus):
    self.corpus = corpus

  def register_cr_score_cache(self, cr_score_cache):
    self.cr_score_cache = cr_score_cache

  def register_diff_cache(self, diff_cache):
    self.diff_cache = diff_cache

  def register_cached_fn(self, name, cached_fn):
    self.cache_list.append((name, cached_fn))

  def cache_info(self):
    cache_info = ''.join([f'\n\t{name}: {cached_fn.cache_info()}' for (name, cached_fn) in self.cache_list])
    return cache_info

  # Internal

  def _status_string(self):
    return (f'Progress: \n' +
            f'  Solution Count: {self.solution_count}\n' +
            f'  Guess Count: {self.guess_count}\n' +
            f'Start Time: {self.time_str(self.start_time)} \n' +
            f'Dictionary Size: {len(self.corpus)}\n' +
            f'Stats: \n' +
            f'   CR Score Cache Size: {len(self.cr_score_cache)}\n' +
            f'   Diff Cache Size: {len(self.diff_cache)}\n' +
            f'   Cache Info: {self.cache_info()}')

  def _print_status_string(self):
    print(self._status_string())

  def _start_timer_thread(self):
    self.timer = RepeatTimer(self._INTERVAL, self._print_status_string)
    self.timer.start()

  def _stop_timer_thread(self):
    self._print_status_string()
    self.timer.cancel()

  def time_str(self, time):
    time.strftime("%H:%M:%S")


class DummyProfiler:
  pass

  def __getattribute__(self, name):
    return lambda *args, **kw: None

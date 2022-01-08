from datetime import datetime
from timer import RepeatTimer


class ProfilerFactory:
  def getProfiler(enabled):
    if enabled:
      return Profiler()
    else:
      return DummyProfiler()


class Profiler:
  solution_count = 0
  guess_count = 0
  start_time = None
  stop_time = None
  timer = None
  corpus = None
  cr_score_cache = None
  diff_cache = None

  def start(self):
    self.start_time = datetime.now()
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

  def register_corpus(self, corpus):
    self.corpus = corpus

  def register_cr_score_cache(self, cr_score_cache):
    self.cr_score_cache = cr_score_cache

  def register_diff_cache(self, diff_cache):
    self.diff_cache = diff_cache

  # Internal

  def _status_string(self):
    return (f'Progress: \n' +
            f'  Solution Count: {self.solution_count}\n' +
            f'  Guess Count: {self.guess_count}\n' +
            f'Start Time: {self.time_str(self.start_time)} \n' +
            f'Dictionary Size: {len(self.corpus)}\n' +
            f'Stats: \n' +
            f'   CR Score Cache Size: {len(self.cr_score_cache)}\n' +
            f'   Diff Cache Size: {len(self.diff_cache)}')

  def _print_status_string(self):
    print(self._status_string())

  def _start_timer_thread(self):
    self.timer = RepeatTimer(5, self._print_status_string)
    self.timer.start()

  def _stop_timer_thread(self):
    self.timer.cancel()

  def time_str(self, time):
    time.strftime("%H:%M:%S")


class DummyProfiler:
  pass

  def __getattribute__(self, name):
    return lambda *args, **kw: None

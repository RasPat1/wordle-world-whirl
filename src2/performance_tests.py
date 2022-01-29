from src2 import MinimalPath
from src import Reader
import cProfile


class PerformanceTests:
  def test_mp_search():
    path = './data/large_test_set_1'
    corpus, _ = Reader.load_lists(path, path)
    print(f'Corpus Size: {len(corpus)}')
    corpus = sorted(corpus)
    result = MinimalPath.best_guess(corpus)
    print(result)
    # Doubling the corpus size 10x the run time. lol i'm effed.


cProfile.run('PerformanceTests.test_mp_search()')

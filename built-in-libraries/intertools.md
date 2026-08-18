# Intertools

* Functions creating iterators for efficient looping
* Reference:  https://docs.python.org/3/library/itertools.html

This module implements a number of [iterator](https://docs.python.org/3/glossary.html#term-iterator) building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.


## Infinite iterators

| Iterator                                                     | Arguments       | Results                                        | Example                               |
| ------------------------------------------------------------ | --------------- | ---------------------------------------------- | ------------------------------------- |
| [`count()`](https://docs.python.org/3/library/itertools.html#itertools.count "itertools.count") | [start[, step]] | start, start+step, start+2*step, …             | `count(10) → 10 11 12 13 14 ...`      |
| [`cycle()`](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle") | p               | p0, p1, … plast, p0, p1, …                     | `cycle('ABCD') → A B C D A B C D ...` |
| [`repeat()`](https://docs.python.org/3/library/itertools.html#itertools.repeat "itertools.repeat") | elem [,n]       | elem, elem, elem, … endlessly or up to n times | `repeat(10, 3) → 10 10 10`            |


## Iterators terminating on the shortest input sequence:

| Iterator                                                     | Arguments                   | Results                                         | Example                                                  |
| ------------------------------------------------------------ | --------------------------- | ----------------------------------------------- | -------------------------------------------------------- |
| [`accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate") | p [,func]                   | p0, p0+p1, p0+p1+p2, …                          | `accumulate([1,2,3,4,5]) → 1 3 6 10 15`                  |
| [`batched()`](https://docs.python.org/3/library/itertools.html#itertools.batched "itertools.batched") | p, n                        | (p0, p1, …, p_n-1), …                           | `batched('ABCDEFG', n=3) → ABC DEF G`                    |
| [`chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain "itertools.chain") | p, q, …                     | p0, p1, … plast, q0, q1, …                      | `chain('ABC', 'DEF') → A B C D E F`                      |
| [`chain.from_iterable()`](https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable "itertools.chain.from_iterable") | iterable                    | p0, p1, … plast, q0, q1, …                      | `chain.from_iterable(['ABC', 'DEF']) → A B C D E F`      |
| [`compress()`](https://docs.python.org/3/library/itertools.html#itertools.compress "itertools.compress") | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), …               | `compress('ABCDEF', [1,0,1,0,1,1]) → A C E F`            |
| [`dropwhile()`](https://docs.python.org/3/library/itertools.html#itertools.dropwhile "itertools.dropwhile") | predicate, seq              | seq[n], seq[n+1], starting when predicate fails | `dropwhile(lambda x: x<5, [1,4,6,4,1]) → 6 4 1`          |
| [`filterfalse()`](https://docs.python.org/3/library/itertools.html#itertools.filterfalse "itertools.filterfalse") | predicate, seq              | elements of seq where predicate(elem) fails     | `filterfalse(lambda x: x%2, range(10)) → 0 2 4 6 8`      |
| [`groupby()`](https://docs.python.org/3/library/itertools.html#itertools.groupby "itertools.groupby") | iterable[, key]             | sub-iterators grouped by value of key(v)        |                                                          |
| [`islice()`](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice") | seq, [start,] stop [, step] | elements from seq[start:stop:step]              | `islice('ABCDEFG', 2, None) → C D E F G`                 |
| [`pairwise()`](https://docs.python.org/3/library/itertools.html#itertools.pairwise "itertools.pairwise") | iterable                    | (p[0], p[1]), (p[1], p[2])                      | `pairwise('ABCDEFG') → AB BC CD DE EF FG`                |
| [`starmap()`](https://docs.python.org/3/library/itertools.html#itertools.starmap "itertools.starmap") | func, seq                   | func(*seq[0]), func(*seq[1]), …                 | `starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000`       |
| [`takewhile()`](https://docs.python.org/3/library/itertools.html#itertools.takewhile "itertools.takewhile") | predicate, seq              | seq[0], seq[1], until predicate fails           | `takewhile(lambda x: x<5, [1,4,6,4,1]) → 1 4`            |
| [`tee()`](https://docs.python.org/3/library/itertools.html#itertools.tee "itertools.tee") | it, n                       | it1, it2, … itn splits one iterator into n      |                                                          |
| [`zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest "itertools.zip_longest") | p, q, …                     | (p[0], q[0]), (p[1], q[1]), …                   | `zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-` |


## Combinatoric iterators

| terator                                                      | Arguments          | Results                                                      |
| ------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| [`product()`](https://docs.python.org/3/library/itertools.html#itertools.product "itertools.product") | p, q, … [repeat=1] | cartesian product, equivalent to a nested for-loop           |
| [`permutations()`](https://docs.python.org/3/library/itertools.html#itertools.permutations "itertools.permutations") | p[, r]             | r-length tuples, all possible orderings, no repeated elements |
| [`combinations()`](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations") | p, r               | r-length tuples, in sorted order, no repeated elements       |
| [`combinations_with_replacement()`](https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement "itertools.combinations_with_replacement") | p, r               | r-length tuples, in sorted order, with repeated elements     |

### Examples

| Examples                                   | Results                                           |
| ------------------------------------------ | ------------------------------------------------- |
| `product('ABCD', repeat=2)`                | `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD` |
| `permutations('ABCD', 2)`                  | `AB AC AD BA BC BD CA CB CD DA DB DC`             |
| `combinations('ABCD', 2)`                  | `AB AC AD BC BD CD`                               |
| `combinations_with_replacement('ABCD', 2)` | `AA AB AC AD BB BC BD CC CD DD`                   |
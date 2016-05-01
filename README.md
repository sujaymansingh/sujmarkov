# sujmarkov

A markov generator (in python!)


## Installation

```pip install git+https://github.com/sujaymansingh/sujmarkov.git```


## Usage (words)

```python
>>> import sujmarkov
>>> m = sujmarkov.Markov(n=2)
>>> for word in ["Warne", "Warwick", "Warsaw", "Arrington", "Williams", "Willis"]:
...   m.add(word)
...
['W', 'a', 'm', 's']
>>>
```

Note: `generate` always returns a list. So when dealing with words, you might want to use `join`.
```python
>>> "".join(m.generate())
'Wick'
```


## Usage (sentences)

```python
>>> import sujmarkov
>>> m = sujmarkov.Markov(n=2)
>>> m.add(["I", "have", "no", "idea"])
>>> m.add(["Don't", "have", "a", "cow", "man"])
>>> m.add(["I", "have", "a", "dog"])
>>> m.generate()
['I', 'have', 'a', 'cow', 'man']
>>>
```

Note: it will be case sensitive, so perhaps you might want to lower case your input before hand.
In fact, it might be worth stripping out punctuation etc. (Have a play around!)


## from_file util

If you have a text file (with one sentence per line), then you can use the `from_file` utility to generate sentences.

```
$ cat sample.txt
You can use a file
One sentence per line.

$ python -m sujmarkov.from_file generate 1 lines from sample.txt
you can use a file
```

(Of course, you may want to use a better sample file...)

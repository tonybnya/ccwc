# Build My Own wc Tool

_**NB:** First of all, this script uses Python 3.8.2_

This challenge is to build my own version of the Unix command line tool `wc`.

## The Challenge - Build wc

The functional requirements for `wc` are concisely described by its `man` page - give it a go in a local terminal:

```sh
man wc
```

The TL/DR version is: **wc** - word, line, character, and byte count.

There are 2 text files, `test.txt`, and `usage.txt`, used to check the behavior of the original `wc` and my version, `ccwc`.

---

Write a simple version of `wc`, let’s call it `ccwc` (cc for Coding Challenges).
---

1. flag `-c` = number of bytes in a file

The output should match this:
```sh
wc -c test.txt
  342190 test.txt

wc -c test.txt usage.txt
  342190 test.txt
    1152 usage.txt
  343342 total
```

```sh
python3 ccwc.py -c test.txt
  342190 test.txt

python3 ccwc.py -c test.txt usage.txt
  342190 test.txt
    1152 usage.txt
  343342 total
```


2. flag `-l` = number of lines in a file

The output should match this:

```sh
wc -l test.txt
  7145 test.txt

wc -l test.txt usage.txt
  7145 test.txt
    27 usage.txt
  7172 total
```

```sh
python3 ccwc.py -l test.txt
  7145 test.txt

python3 ccwc.py -l test.txt usage.txt
  7145 test.txt
    27 usage.txt
  7172 total
```


3. flag `-m` = number of characters in a file

The output should match this:

```sh
wc -m test.txt
  339292 test.txt

wc -m test.txt usage.txt
  339292 test.txt
    1152 usage.txt
  340444 total
```

```sh
python3 ccwc.py -m test.txt
  339292 test.txt

python3 ccwc.py -m test.txt usage.txt
  339292 test.txt
    1152 usage.txt
  340444 total
```


4. flag `-w` = number of words in a file

The output should match this:

```sh
wc -w test.txt
  58164 test.txt

wc -w test.txt usage.txt
  58164 test.txt
    168 usage.txt
  58332 total
```

```sh
python3 ccwc.py -w test.txt
  58164 test.txt

python3 ccwc.py -w test.txt usage.txt
  58164 test.txt
    168 usage.txt
  58332 total
```


5. No flag = `-l`, `-w`, and `-c` together

The output should match this:

```sh
wc test.txt
  7145 58164 342190 test.txt

wc test.txt usage.txt
  7145 58164 342190 test.txt
    27   168   1152 usage.txt
  7172 58332 343342 total
```

```sh
python3 ccwc.py test.txt
  7145 58164 342190 test.txt

python3 ccwc.py test.txt usage.txt
  7145 58164 342190 test.txt
    27   168   1152 usage.txt
  7172 58332 343342 total
```


6. No argument = read from standard input

```sh
cat test.txt | wc -l
  7145
```

```sh
cat test.txt | python3 ccwc.py -l
  7145
```

# Build My Own wc Tool

This challenge is to build my own version of the Unix command line tool `wc`.

## The Challenge - Build wc

The functional requirements for `wc` are concisely described by its `man` page - give it a go in a local terminal:

```sh
man wc
```

The TL/DR version is: **wc** - word, line, character, and byte count.

There is a text file named `test.txt` used to test the solution.

---

Write a simple version of `wc`, let’s call it `ccwc` (cc for Coding Challenges).
---

1. Command line option `-c` and outputs the number of bytes in a file.

The output should match this:

```sh
> ./ccwc -c test.txt
342190 test.txt
```
---

2. Command line option `-l` that outputs the number of lines in a file.

The output should match this:

```sh
> ./ccwc -l test.txt
7145 test.txt
```
---

3. Command line option `-w` that outputs the number of words in a file.

The output should match this:

```sh
> ./ccwc -w test.txt
58164 test.txt
```
---

4. Command line option `-m` that outputs the number of characters in a file.

The output should match this:

```sh
> ./ccwc -m test.txt
339292 test.txt
```
---

5. This step's goal is to support the default option - i.e. no options are provided, which is the equivalent to the `-c`, `-l`, and `-w` options.

The output should match this:

```sh
> ./ccwc test.txt
7145 58164 342190 test.txt
```

6. The Final Step
In this step the goal is to support being able to read from standard input if no filename is specified.

```sh
> cat test.txt | ./ccwc -l
7145
```

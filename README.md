# ctd

compare the difference!

ctd takes two strings and compares the difference. This is pretty easily done in python. However, ctd aims to make it easier by showing the original strings and then where the difference lies, using color indicators.

# Installation
python3 setup.py install

# Usage
```
ctd example123 example345
```
![example](https://github.com/DFC302/ctd/blob/master/pics/example.png)

# Usage cases
Say you are working on a piece of code, but you are getting a syntax error. The code looks right to the code you copied, but something must be off. Use CTD. (Warning: Since CTD is running through a terminal, you will need to escape your comparisons with double or single quotes. If quotes are already present, the opposite quotations can be used, or simply escape them with a forward slash)

* Example 1: You have similar strings. However, you keep getting an error on example1 string. You keep getting the following erorr:
```
example1 = " ".join([a.strip( for a in b.split("\n") if a])
  File "<stdin>", line 1
    example1 = " ".join([a.strip( for a in b.split("\n") if a])
```
Your new to the language and maybe its hard to figure out where you went wrong. CTD to the rescue!
```
original =  example1 = " ".join([a.strip( for a in b.split("\n") if a])
comparison = example2 = " ".join([a.strip() for a in b.split("\n") if a])
```
* COMMAND: 
```
ctd 'example1 = " ".join([a.strip( for a in b.split("\n") if a])' 'example2 = " ".join([a.strip() for a in b.split("\n") if a])'
```

* Expected output:
![example_1](https://github.com/DFC302/ctd/blob/master/pics/Screenshot%20from%202020-05-09%2010-23-21.png)

As we can see, CTD shows us where the difference is in red.





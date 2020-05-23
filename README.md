# ctd

compare the difference!

ctd takes two strings and compares the difference. This is pretty easily done in python. However, ctd aims to make it easier by showing the original strings and then where the difference lies, using color indicators.

# Installation
python3 setup.py install

# Usage
```
ctd 098f6bcd4621d373cade4e832627b4f6 098f6bcd462d373cade4e832627b4f6
```
![example](https://github.com/DFC302/ctd/blob/master/pics/example.png)

# Notes
Since bash (or whatever shell you use) will interpert some strings certain ways, when using *ctd* you may need to surround your comparisions in quotes. 

Example:

```
ctd test\n test
```
Result:

![example2](https://github.com/DFC302/ctd/blob/master/pics/example2.png)

Escaping this example in quotes like so:
```
ctd "test\n" test
```
Result:

![example3](https://github.com/DFC302/ctd/blob/master/pics/example3.png)

Another example, say you have a quote in your comparison. Like so:
```
ctd test"test test
```
This will cause an error in the shell. You can easily surround it in opposite quotes or escape it like so:
```
ctd 'test"test' test
ctd test\"test test
```
Result:

![example4](https://github.com/DFC302/ctd/blob/master/pics/example4.png)





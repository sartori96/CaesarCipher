# CaesarCipher

This project implements a Caesar Cipher, allowing the user to encode or decode messages by shifting the alphabet by a specified number of positions.

## Download the repository and open the terminal in the project
```shell
$ git clone https://github.com/sartori96/CaesarCipher
$ cd CaesarCipher
```

How to install

Enter the following commands
```shell
$ python -m venv /path/to/new/virtual/environment
$ source <venv>/<bin or Scripts>/activate
$ pip install -r requirements.txt
```

How to use

Enter the following commands
```shell
$ python CaesarCipher.py
```

Example
```shell
Type 'encode' to encrypt, type 'decode' to decrypt and 'exit' to leave:
encode
Type your message:
hello world
Type the shift number:
3
Result: khoor zruog
```

The program logs all results in a CaesarCipher.log file and also displays them in the terminal.
```txt
2024-09-07 15:09:11,882 - INFO - Started
2024-09-07 15:09:24,773 - INFO - Result: khoor zruog
2024-09-07 15:09:40,527 - INFO - Exiting the program.
```
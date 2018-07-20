# cryptoexamples
Some basic examples of public key cryptography and the math behind the scenes using python. Please note that mileage may very, use only for testing and education. I would not recommend using these for anything else as I am not a cryptographer. 


## Dependencies
You will need pycryptodome: https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

pip install pycryptodome

## How To
The scratchgenrsa.py is where most of the fun is at. No input is required, simply execute the script and you will get two files, a public and private key pair.
There are some other scripts in here that allow you to check for primes, semiprimes, and do some encrypt/decrypt using a well known library, pycryptodome.

Please note that the scratchgenrsa.py will let you generate a key length of ANY size. This can be fun for testing, but please always use a minimum key size of 2048 for anything outside of testing.

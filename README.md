# Python implementations speed test

A project concerned with comparing speeds of different python low-level language integrations.

## Tested implementations
* Pure python

Using core python language features and nothing else.

* Numpy

Using built in functions from the numpy library

* CPU PyTorch

Using built in function from pytorch library on cpu

* Cython pure

Compiling the pure python script as a cython library and importing it

* Cython C

Adding cython (C) language features to the pure python implementation.

* Ctypes C

Using the ctypes module to load in a dll (so) written in C and compiled

* Ctypes Rust

Using the ctypes module to load in a dll (so) written in Rust and compiled

## Test cases
* rootloop

Compute the sum of the square root of every even number up to N.
## Setup
Run `build.sh`.

## Usage
Run `run.py`.

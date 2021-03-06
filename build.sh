#!/bin/bash
cd "$(dirname "$0")"

# Cython
cd src/cython_pure_src
python3 setup.py build_ext --inplace
cd ../cython_c_src
python3 setup.py build_ext --inplace

# C
cd ../c_src
gcc -shared -o lib.so lib.c -O3 -lm -fPIC

# Rust
cd ../rust_src
cargo update
cargo build --release

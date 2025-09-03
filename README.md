## Numpy-Fundamentals-in-Pytorch
This repository contains a comprehensive NumPy tutorial for beginners and intermediate users. It covers array creation, indexing, slicing, reshaping, mathematical operations, boolean masking, conditional selection, and random number generation. Each section includes explanations and examples.

#Contents

Creating Arrays

Converting Python lists to NumPy arrays

Using np.array(), np.zeros(), np.ones(), np.full(), np.arange()

Array Operations

Element-wise operations: +, -, *, /

Mathematical functions: np.sqrt(), np.exp(), np.absolute()

Sign detection: np.sign() returns -1 for negatives, 0 for zero, and 1 for positives

Indexing and Slicing

1D and 2D slicing

Steps in slicing (e.g., arr[::2])

Boolean indexing

Reshaping and Flattening

reshape() to change array dimensions

flatten() or reshape(-1) to convert multi-dimensional arrays to 1D

Conditional Selection

np.where(condition, x, y) to select values based on condition

Example: select elements greater than a threshold or replace others

Sorting and Iterating

np.sort() for sorting arrays

Iterating with np.nditer()

Summing along axes using np.sum(axis=...)

Random Numbers

np.random.default_rng() for random number generation

integers(), uniform() for generating random ints or floats

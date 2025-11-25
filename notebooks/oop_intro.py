# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Introduction to object oriented programming in Python

# %% [markdown]
# **Task** Implement a class `ComplexNumber` describing complex numbers. It should have methods `__add__` (addition), `__mul__` (multiplication), `__abs__` (module of a complex number); *n*-th root. 
#
# Provide examples of usage. 

# %% [markdown]
# $$ \phi = 2 \mathrm{arctan} \left( \frac{y}{\sqrt{x^2 + y^2} + x} \right)  \quad y \neq 0 \textrm{ or } x \geq 0$$

# %%
# %load_ext nb_mypy

# %%
import math


# %%
class ComplexNumber:

    real: float
    imag: float

    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':

        if not isinstance(other, ComplexNumber):
            raise ValueError('The second argument should be a complex number')

        return type(self)(self.real + other.real, self.imag + other.imag)
        
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return ComplexNumber(r, i)

    def __abs__(self) -> float:
        return math.sqrt(self.real**2 + self.imag**2)

    @property
    def angle(self) -> float:
        return math.atan2(self.imag, self.real)

    def nth_root(self, n) -> list:
        r = abs(self)
        theta = self.angle

        starting_angle = theta / n
        magnitude = r ** (1 / n)

        angles = [starting_angle + 2 * math.pi * k / n for k in range(n)]
        roots = [ComplexNumber(magnitude * math.cos(angle),
                               magnitude * math.sin(angle)) for angle in angles]
        return roots



# %%
class RealNumber(ComplexNumber):

    def __init__(self, value: float, imag=0):
        super().__init__(real=value, imag=0)

    def __add__():
        pass
    


# %%
x1 = RealNumber(3)

# %%
x1

# %%
x2 = RealNumber(4)

# %%
type(x1 + x2)

# %%
x1.angle

# %%
RealNumber(-4).angle

# %%
RealNumber(-4).nth_root(2)

# %%

# %%

# %%

# %%

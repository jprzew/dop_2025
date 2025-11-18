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
# # My first notebook

# %%
# %load_ext nb_mypy

# %% [markdown]
# ## Type annotations

# %% [markdown]
# The Python language allows us to annotate variable types. For example we may want `name` to be a string variable and `age` to be integer variable.  

# %%
name: str
age: int

# %%
name = 'Jan'


# %% [markdown]
# ## Annotating functions

# %%
def factorial(n: int) -> int:
    if n > 0: 
        return factorial(n-1) * n

    return 1


# %%
factorial(2)

# %%
factorial('hello')

# %%

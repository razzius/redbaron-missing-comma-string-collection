This is a Python script to warn you when you have a collection of strings that is missing commas which will perform implicit concatenation.

For example,

```python
[
    'a'
    'b'
]
```

is usually meant to be

```python
[
    'a',
    'b'
]
```

however Python will interpret it as


```python
[
    'ab'
]
```

which usually isn't what you want.

This script will warn you about such code:

```sh
$ python missing_commas_string_collection.py example_violation/basic.py
example_violation/basic.py:2:8: C101 ElementMissingComma: Implicit string concatenation in collection
```

# Installation

```sh
git clone https://github.com/razzius/redbaron-missing-comma-string-collection
cd redbaron-missing-comma-string-collection
pip install -r requirements.txt
```

# Usage

```
python missing_commas_string_collection.py example_violation/basic.py
```

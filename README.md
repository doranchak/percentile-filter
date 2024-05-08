# percentile-filter
Python script that takes a list of numbers and output only the ones that contribute to some percentage threshold of their total sum.

Useful for tasks such as taking a list of words and their frequencies, and filtering out the uncommon words.

Usage:

```
python percentile-filter.py [filename] [percentage]
```

For example:

```
python percentile-filter.py sample.txt 95
```


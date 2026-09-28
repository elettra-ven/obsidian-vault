The program doesn't know beforehand how many extractions will be performed. There often is a condition that has to be satisfied for the iteration to be considered completed, however, this can result in infinite loops.

## `while` command
The iteration continues as long as the expression in the *guard* is evaluated as `True`.

We can approximate some bounded iterations to unbounded iterations:
```
for i in range(len(s)):
	<body>
```

```
i = 0
while i < len(s):
	<body>
	i = i+1
```

The unbounded iteration does not "freeze" neither `s` nor its length.



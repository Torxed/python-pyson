# python-pyson

Like JSON, byt for Python.<br>
Supports any `eval()` in `key` and `value` pairs.<br>
*(So don't go around using it in production)*

# Example

```python
import time
import random

import pyson

content = """
{
	"time" : time.time(),
	random.randint(0, 1) : "a random number",
	"another_level" : {
		"test" : 5
	},
	"main level" : True
}
"""

print(pyson.loads(content, globals(), locals()))
```

Produces:

```python
{
	'time': 1604261222.4304745,
	1: 'a random number',
	'another_level': {
		'test': 5
	},
	'main level': True
}
```

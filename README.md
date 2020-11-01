# python-pyson

Like JSON, byt for Python.<br>
Supports any `ast.literal_eval` in `key` and `value` pairs.

# Example

```
import time
import random

{
	"time" : time.time(),
	random.randint(0, 10) : "a random number"
}
```

Produces:

```
{
	"time" : 1604257863.0922215,
	5 : "a random number"
}
```
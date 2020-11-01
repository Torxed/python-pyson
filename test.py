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
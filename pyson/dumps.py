import io

orig_globals = globals
orig_locals = locals 

def load(file, globals=None, locals=None, *args, **kwargs):
	orig_globals().update(globals)
	orig_locals().update(locals)

	struct = None
	pointer = None
	last_level = []

	for line in file:
		line = line.strip()

		if line.strip() == '{':
			struct = {}
			pointer = struct

		elif type(struct) is dict and ':' in line:
			key, val = line.split(':', 1)
			key, val = key.strip(' ,;\r\n'), val.strip(' ,;\r\n')

			key = eval(key)
			if val == '{':
				pointer[key] = {}
				last_level.append(pointer) # Not efficient
				pointer = pointer[key]
			else:
				val = eval(val)
				pointer[key] = val

		elif line.strip(' ,;\r\n') in ('}', '},'):
			if len(last_level):
				pointer = last_level.pop()
			else:
				break

	return struct

def loads(string, *args, **kwargs):
	return load(io.StringIO(string), *args, **kwargs)
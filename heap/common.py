import gdb

def to_int(value):
  try: 
    return int(value.cast(gdb.lookup_type('long')))
  except Exception:
    pass
  return int(value)

def to_long(value):
  try:
    return long(str(value), 16)
  except Exception:
    pass
  try:
    return long(value.cast(gdb.lookup_type('unsigned long')))
  except Exception:
    pass
  return long(value)

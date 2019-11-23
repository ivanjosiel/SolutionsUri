def read_string():
      try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


if len(read_string()) <= 80:
  print("YES")
else:
  print("NO")
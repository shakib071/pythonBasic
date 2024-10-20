
def func(k):
    if k==0 : return 0
    return k+func(k-1)

print(func(10))


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
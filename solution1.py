def count_down(n):

  # Base case
  if n == 0:
      return 0

  # Recursive case
  else:
      print(n)
      count_down(n-1)

# test case
n=10
print (count_down(n))

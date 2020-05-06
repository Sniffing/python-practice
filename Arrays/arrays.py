import numpy

def initArray():
  allZeros = [0] * 10
  # print(allZeros)

  allNulls = [None] * 10
  # print(allNulls)

  incrementing = [x for x in range(10)]
  # print(incrementing)

  twoDimArray = [[x*y for x in range(10)]
                    for y in range(5)]
  # print(twoDimArray)

  numpyArray = numpy.empty(4, dtype=object)
  # print(numpyArray)

  unsorted = [3,5,3,6,57,5,1,9,7]
  unsorted.sort()
  # print(unsorted)

  unsorted.sort(reverse=True)
  # print(unsorted)

  tuples = [(x, ord('A') + x, chr(ord('A') + x)) for x in range(10)]
  # print(tuples)

  t1 = tuples.copy()
  t1 = list(map(lambda t: int(str(t[0]) + str(t[1])), t1))
  # print(t1)

  getLast = t1[-1]
  # print(getLast)

  getRange = t1[4:]
  # print(getRange)

  getRange1 = t1[4:-1]
  # print(getRange1)

  getRange2 = t1[4:-2]
  # print(getRange2)

  remove = t1.copy()
  remove3 = remove.pop(-2)
  # print(remove3)
  # print(remove)

  nums = [x for x in range(20)]
  evens = nums[::2]
  print(evens)
  print(nums[::-1])

  delete = nums.copy()
  del delete[::3]
  print(delete)

print('Initialising arrays')
initArray()
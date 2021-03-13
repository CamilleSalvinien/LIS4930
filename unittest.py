import itertools
import unittest

def iteration(name):
  count = 0
  lista = []
  for i in itertools.cycle(name):
    if count > 10:
      break
    else:
      lista.append(i)
      count += 1  
  return lista

class testIteration(unittest.TestCase):
  def testIterationsuccess(self):
    actual = iteration(name = "Potatoes")
    expected = ['T','O','M','A','T', 'O','E','S','T']
    self.assertEqual(actual,expected,)

if __name__ == '__main__':
  unittest.main()
 
 def repeat(number,times):
  nums = list(itertools.repeat(number,times))
  return nums

class testIteration(unittest.TestCase):
  def testIterationsuccess(self):
    actual = repeat(number = 3, repeat = 2)
    expected = [3, 3]
    self.assertEqual(actual,expected)

if __name__ == '__main__':
  unittest.main()

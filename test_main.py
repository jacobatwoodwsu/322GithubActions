from main import add

def testAdd():
  assert add(2,3) == 5
  assert add(-1,1) == 0
  assert add(0,0) == 0

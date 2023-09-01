import pytest
def add(a,b):
  return a + b
def test_add(1,2):
  assert add(1,2) == 3

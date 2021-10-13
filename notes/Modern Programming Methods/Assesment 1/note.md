## **Reading List**

  - [Leetcode Game of Life](https://leetcode.com/problems/game-of-life/)
  - [Numpy Game of Life](https://github.com/rougier/numpy-tutorial/blob/master/scripts/game-of-life-python.py)

## Coding tips & Trouble shooting

```python
""" Python: Apply convolution on matrix """
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
np.sum(kernel * matrix)

"""Pentagonal Game of Life"""
Hint: For each grid, find the pattern of its neighbors. Is the pattern related to the index of this grid?

"""Test cases for Lorenz96 model"""
case1: X = [8.0,9.0,8.0,8.0], nsteps = 1
expect: [7.920792079207921, 8.990099009900991, 7.992949633165454, 8.084622935043805]
    
    
""" Test cases for Game of Life model"""
# Blinker
case: X_1 = [[False,False,False,False,False],[False,False,False,False,False],[False,True,True,True,False],[False,False,False,False,False],[False,False,False,False,False]]

expect: (1 generation)
dead-bound:
[[False False False False False]
 [False False  True False False]
 [False False  True False False]
 [False False  True False False]
 [False False False False False]]


case: X_2 = [[False,True,True,True,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
    
expect: (1 generation)
periodic-bound:
[[False False  True False False]
 [False False  True False False]
 [False False False False False]
 [False False False False False]
 [False False  True False False]]

# Glider
case: X_3 = [[False,False,False,False,False],[False,True,True,True,False],[False,False,False,True,False],[False,False,True,False,False],[False,False,False,False,False]]
    
expect:(4 generation)  
 [[False False  True  True  True]
 [False False False False  True]
 [False False False  True False]
 [False False False False False]
 [False False False False False]]

```

![](https://d3i71xaburhd42.cloudfront.net/330535fb0ef0208b050483453c6c489c2f23f059/6-Figure6-1.png)


## **Reading List**

  - [pdb example](https://www.youtube.com/watch?v=bHx8A8tbj2c&ab_channel=RealPython)
  - [segmentation fault](https://stackoverflow.com/questions/2346806/what-is-a-segmentation-fault)
  - [gdb tutorial](https://www.cs.umd.edu/~srhuang/teaching/cmsc212/gdb-tutorial-handout.pdf)
  - [High Performance Computing Course](https://www.youtube.com/watch?v=SH7qhC1tJmA&list=PLmJwSK7qduwVnlrIPjrfSn7QRcv3wIQj5&ab_channel=ProfDr-IngMorrisRiedel)

## Coding tips & Trouble shooting

```bash
# Example 1:
(ese-msc) sm321@IC-C17G96QPQ6L4 files % ipython
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: run index_error.py
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
~/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py in <module>
      6 
      7 if __name__ == '__main__':
----> 8     index_error()
      9 

~/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py in index_error()
      3 def index_error():
      4     lst = list('foobar')
----> 5     print(lst[len(lst)])
      6 
      7 if __name__ == '__main__':

IndexError: list index out of range

In [2]: debug
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py(5)index_error()
      3 def index_error():
      4     lst = list('foobar')
----> 5     print(lst[len(lst)])
      6 
      7 if __name__ == '__main__':

ipdb> list
      1 """Small snippet to raise an IndexError."""
      2 
      3 def index_error():
      4     lst = list('foobar')
----> 5     print(lst[len(lst)])
      6 
      7 if __name__ == '__main__':
      8     index_error()
      9 

ipdb> len(lst)
6
ipdb> print(lst[len(lst)-1])
r
ipdb> quit

In [3]: 
  
# Example 2: Post-mortem debugging without IPython, I think you can do this when you do not have access to the code?

(ese-msc) sm321@IC-C17G96QPQ6L4 files % python -m pdb index_error.py
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py(1)<module>()
-> """Small snippet to raise an IndexError."""
(Pdb) continue
Traceback (most recent call last):
  File "/Users/sm321/opt/anaconda3/envs/ese-msc/lib/python3.9/pdb.py", line 1723, in main
    pdb._runscript(mainpyfile)
  File "/Users/sm321/opt/anaconda3/envs/ese-msc/lib/python3.9/pdb.py", line 1583, in _runscript
    self.run(statement)
  File "/Users/sm321/opt/anaconda3/envs/ese-msc/lib/python3.9/bdb.py", line 580, in run
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "/Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py", line 1, in <module>
    """Small snippet to raise an IndexError."""
  File "/Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py", line 5, in index_error
    print(lst[len(lst)])
IndexError: list index out of range
Uncaught exception. Entering post mortem debugging
Running 'cont' or 'step' will restart the program
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/index_error.py(5)index_error()
-> print(lst[len(lst)])
(Pdb) 

# Example 3: step-by-step execution (iPython)
In [3]: run -d wiener_filtering.py
*** Blank or comment
*** Blank or comment
*** Blank or comment
*** Blank or comment
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(1)<module>()
----> 1 """ Wiener filtering a noisy racoon face: this module is buggy
      2 """
      3 
      4 import numpy as np
      5 import scipy as sp

ipdb> n
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(4)<module>()
      2 """
      3 
----> 4 import numpy as np
      5 import scipy as sp
      6 import matplotlib.pyplot as plt

ipdb> b 34
Breakpoint 1 at /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py:34
ipdb> c
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(34)iterated_wiener()
     32         Do not use this: this is crappy code to demo bugs!
     33     """
1--> 34     noisy_img = noisy_img
     35     denoised_img = local_mean(noisy_img, size=size)
     36     l_var = local_var(noisy_img, size=size)

ipdb> s
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(35)iterated_wiener()
     33     """
1    34     noisy_img = noisy_img
---> 35     denoised_img = local_mean(noisy_img, size=size)
     36     l_var = local_var(noisy_img, size=size)
     37     for i in range(3):

ipdb> n
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(36)iterated_wiener()
1    34     noisy_img = noisy_img
     35     denoised_img = local_mean(noisy_img, size=size)
---> 36     l_var = local_var(noisy_img, size=size)
     37     for i in range(3):
     38         res = noisy_img - denoised_img

ipdb> n
> /Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py(37)iterated_wiener()
     35     denoised_img = local_mean(noisy_img, size=size)
     36     l_var = local_var(noisy_img, size=size)
---> 37     for i in range(3):
     38         res = noisy_img - denoised_img
     39         noise = (res**2).sum()/res.size

ipdb> print(l_var)
[[2008 2839 3608 ... 2413 3262 3585]
 [1753  934  790 ...  335  375 3791]
 [1312  572  500 ...  458  332 3296]
 ...
 [2395  581  271 ...  426  445 4390]
 [2300  743  145 ...  484  313 4207]
 [2328 2691 3200 ... 3592 4157 4377]]
ipdb> print(l_var.min())
-27
ipdb> 

# Example 4: set errors to exceptions
(ese-msc) sm321@IC-C17G96QPQ6L4 files % ipython
Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: run wiener_filtering.py
/Users/sm321/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py:40: RuntimeWarning: divide by zero encountered in true_divide
  noise_level = (1 - noise/l_var )

In [2]: import numpy as np

In [3]: np.seterr(all='raise')
Out[3]: {'divide': 'warn', 'over': 'warn', 'under': 'ignore', 'invalid': 'warn'}

In [4]: run wiener_filtering.py
---------------------------------------------------------------------------
FloatingPointError                        Traceback (most recent call last)
~/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py in <module>
     55 plt.matshow(noisy_face[cut], cmap=plt.cm.gray)
     56 
---> 57 denoised_face = iterated_wiener(noisy_face)
     58 plt.matshow(denoised_face[cut], cmap=plt.cm.gray)
     59 

~/ACSE/modern-programming-methods/lectures/lecture10/files/wiener_filtering.py in iterated_wiener(noisy_img, size)
     38         res = noisy_img - denoised_img
     39         noise = (res**2).sum()/res.size
---> 40         noise_level = (1 - noise/l_var )
     41         noise_level[noise_level<0] = 0
     42         denoised_img = denoised_img + noise_level*res

FloatingPointError: divide by zero encountered in true_divide

In [5]: 

# Example 5: GDB --> running on Ubuntu VM machine

# Example 6: Distributed computation using MPI
# Docs for MPI and OpenMP
# https://www.mpi-forum.org/docs/
# https://www.open-mpi.org/doc/
```




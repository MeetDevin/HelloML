# import numpy as np
# from timeit import default_timer as timer
# from numba import vectorize
#
#
# @vectorize(["float32(float32, float32)"], target='cuda')
# def VecADD(a, b):
#     return a+b
#
#
# n = 32000000
# a = np.ones(n, dtype=np.float32)
# b = np.ones(n, dtype=np.float32)
# c = np.zeros(n, dtype=np.float32)
#
# start = timer()
# C = VecADD(a, b)
# print(timer() - start, C)
#
# import pycuda.driver as drv
# import numpy
#
# from pycuda.compiler import SourceModule
#
# mod = SourceModule("""
# __global__  void multiply_them(float *dest, float *a, float *b)
# {
#   const int i = threadIdx.x;
#   dest[i] = a[i] * b[i];
# }
# """)
#
# multiply_them = mod.get_function("multiply_them")
#
# a = numpy.random.randn(400).astype(numpy.float32)
# b = numpy.random.randn(400).astype(numpy.float32)
#
# dest = numpy.zeros_like(a)
# multiply_them(
#         drv.Out(dest), drv.In(a), drv.In(b),
#         block=(400, 1, 1), grid=(1, 1))
#
# print(dest - a * b)

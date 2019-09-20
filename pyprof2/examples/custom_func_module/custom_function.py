#!/usr/bin/env python3

import torch
import torch.cuda.profiler as profiler
import pyprof2
#Initialize pyprof2
pyprof2.init()

class Foo(torch.autograd.Function):
	@staticmethod
	def forward(ctx, in1, in2):
		out = in1 + in2		#This could be a custom C/C++ function.
		return out

	@staticmethod
	def backward(ctx, grad):
		in1_grad = grad		#This could be a custom C/C++ function.
		in2_grad = grad		#This could be a custom C/C++ function.
		return in1_grad, in2_grad

#Hook the forward and backward functions to pyprof2
pyprof2.wrap(Foo, 'forward')
pyprof2.wrap(Foo, 'backward')

foo = Foo.apply

x = torch.ones(4,4).cuda()
y = torch.ones(4,4).cuda()

with torch.autograd.profiler.emit_nvtx():
	profiler.start()
	z = foo(x,y)
	profiler.stop()

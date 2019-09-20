import torch
import fused_adam_cuda
from apex.optimizers import FusedAdam, FP16_Optimizer
import pyprof2

pyprof2.init()
pyprof2.wrap(fused_adam_cuda, 'adam')

model = torch.nn.Linear(10, 20).cuda().half()
criterion = torch.nn.CrossEntropyLoss().cuda()
optimizer = FusedAdam(model.parameters())
optimizer = FP16_Optimizer(optimizer)

x = torch.ones(32, 10).cuda().half()
target = torch.empty(32, dtype=torch.long).random_(20).cuda()
y = model(x)
loss = criterion(y, target)
optimizer.zero_grad()
loss.backward()
optimizer.step()

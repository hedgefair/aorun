from .context import aorun

from aorun.layers import Dense
from aorun.layers import Relu

import torch
import numpy as np


def test_dense_layer_output_dim():
    l = Dense(5, input_dim=10)

    assert l.output_dim == 5


def test_dense_layer_forward():
    x = torch.Tensor(2, 10)
    l = Dense(5, input_dim=10)
    y = l.forward(x)

    assert y.size() == (2, 5)


def test_dense_multiple_layers():
    x = torch.Tensor(2, 10)
    l1 = Dense(5, input_dim=10)
    l2 = Dense(3, input_dim=5)

    y = l1.forward(x)
    assert y.size() == (2, 5)

    y = l2.forward(y)
    assert y.size() == (2, 3)


def test_relu_output_size():
    x = torch.Tensor(2, 2)
    l1 = Dense(3, input_dim=2)
    l2 = Relu()

    y = l1.forward(x)
    y = l2.forward(y)

    assert y.size() == (2, 3)
    assert (y.data >= 0).sum() == np.prod(y.size())
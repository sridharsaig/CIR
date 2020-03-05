#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.


import unittest
import torch

from pytorch3d.structures import utils as struct_utils

from common_testing import TestCaseMixin


class TestStructUtils(TestCaseMixin, unittest.TestCase):
    def test_list_to_padded(self):
        device = torch.device("cuda:0")
        N = 5
        K = 20
        ndim = 2
        x = []
        for _ in range(N):
            dims = torch.randint(K, size=(ndim,)).tolist()
            x.append(torch.rand(dims, device=device))
        pad_size = [K] * ndim
        x_padded = struct_utils.list_to_padded(
            x, pad_size=pad_size, pad_value=0.0, equisized=False
        )

        self.assertEqual(x_padded.shape[1], K)
        self.assertEqual(x_padded.shape[2], K)
        for i in range(N):
            self.assertClose(
                x_padded[i, : x[i].shape[0], : x[i].shape[1]], x[i]
            )

        # check for no pad size (defaults to max dimension)
        x_padded = struct_utils.list_to_padded(
            x, pad_value=0.0, equisized=False
        )
        max_size0 = max(y.shape[0] for y in x)
        max_size1 = max(y.shape[1] for y in x)
        self.assertEqual(x_padded.shape[1], max_size0)
        self.assertEqual(x_padded.shape[2], max_size1)
        for i in range(N):
            self.assertClose(
                x_padded[i, : x[i].shape[0], : x[i].shape[1]], x[i]
            )

        # check for equisized
        x = [torch.rand((K, 10), device=device) for _ in range(N)]
        x_padded = struct_utils.list_to_padded(x, equisized=True)
        self.assertClose(x_padded, torch.stack(x, 0))

        # catch ValueError for invalid dimensions
        with self.assertRaisesRegex(ValueError, "Pad size must"):
            pad_size = [K] * 4
            struct_utils.list_to_padded(
                x, pad_size=pad_size, pad_value=0.0, equisized=False
            )

        # invalid input tensor dimensions
        x = []
        ndim = 3
        for _ in range(N):
            dims = torch.randint(K, size=(ndim,)).tolist()
            x.append(torch.rand(dims, device=device))
        pad_size = [K] * 2
        with self.assertRaisesRegex(ValueError, "Supports only"):
            x_padded = struct_utils.list_to_padded(
                x, pad_size=pad_size, pad_value=0.0, equisized=False
            )

    def test_padded_to_list(self):
        device = torch.device("cuda:0")
        N = 5
        K = 20
        ndim = 2
        dims = [K] * ndim
        x = torch.rand([N] + dims, device=device)

        x_list = struct_utils.padded_to_list(x)
        for i in range(N):
            self.assertClose(x_list[i], x[i])

        split_size = torch.randint(1, K, size=(N,)).tolist()
        x_list = struct_utils.padded_to_list(x, split_size)
        for i in range(N):
            self.assertClose(x_list[i], x[i, : split_size[i]])

        split_size = torch.randint(1, K, size=(2 * N,)).view(N, 2).unbind(0)
        x_list = struct_utils.padded_to_list(x, split_size)
        for i in range(N):
            self.assertClose(
                x_list[i], x[i, : split_size[i][0], : split_size[i][1]]
            )

        with self.assertRaisesRegex(ValueError, "Supports only"):
            x = torch.rand((N, K, K, K, K), device=device)
            split_size = torch.randint(1, K, size=(N,)).tolist()
            struct_utils.padded_to_list(x, split_size)

    def test_list_to_packed(self):
        device = torch.device("cuda:0")
        N = 5
        K = 20
        x, x_dims = [], []
        dim2 = torch.randint(K, size=(1,)).item()
        for _ in range(N):
            dim1 = torch.randint(K, size=(1,)).item()
            x_dims.append(dim1)
            x.append(torch.rand([dim1, dim2], device=device))

        out = struct_utils.list_to_packed(x)
        x_packed = out[0]
        num_items = out[1]
        item_packed_first_idx = out[2]
        item_packed_to_list_idx = out[3]

        cur = 0
        for i in range(N):
            self.assertTrue(num_items[i] == x_dims[i])
            self.assertTrue(item_packed_first_idx[i] == cur)
            self.assertTrue(
                item_packed_to_list_idx[cur : cur + x_dims[i]].eq(i).all()
            )
            self.assertClose(x_packed[cur : cur + x_dims[i]], x[i])
            cur += x_dims[i]

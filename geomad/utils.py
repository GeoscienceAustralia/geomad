# Copyright (c) 2018-2025 Geoscience Australia
# SPDX-License-Identifier: Apache-2.0
import os


def get_max_threads():
    n = os.cpu_count() or 1
    print("Automatically using %i threads." % (n,))
    return n

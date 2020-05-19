#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/13/20
# Testing suite for disks

from disk import Disk, RED, YELLOW


def test_default_disk():
    disk = Disk(20, 20, 200)
    assert disk.width == 200
    assert disk.height == 200
    assert disk.color == RED


def test_other_disk():
    disk = Disk(20, 20, 200, 'yellow')
    assert disk.width == 200
    assert disk.height == 200
    assert disk.color == YELLOW

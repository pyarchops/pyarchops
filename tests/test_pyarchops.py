#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyarchops` package."""

import inspect


def test_pyarchops_imports():
    """Test the pyarchops main package"""

    import pyarchops

    assert inspect.ismodule(pyarchops)

    assert inspect.ismodule(pyarchops.os_updates)
    assert inspect.isfunction(pyarchops.os_updates.apply)

    assert inspect.ismodule(pyarchops.helpers)
    assert inspect.isfunction(pyarchops.helpers.ephemeral_docker_container)

    assert inspect.ismodule(pyarchops.tinc)
    assert inspect.isfunction(pyarchops.tinc.apply)

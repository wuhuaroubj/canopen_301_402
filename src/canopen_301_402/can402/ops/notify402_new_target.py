#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from funcy import partial

from canopen_301_402.constants import *
from canopen_301_402.async.async_chain import AsyncChain
from canopen_301_402.can402.ops.change_controlword import ChangeControlword


class Notify402NewTarget(AsyncChain):
    """docstring for Set402Mode"""
    def __init__(self, node, relative=False, immediatly=False, *args, **kwargs):
        self.node = node
        self.relative = relative
        self.immediatly = immediatly


        notify = partial(ChangeControlword,
                node = self.node,
                updates = {
                    Can402ControlwordBits.new_set_point: True,
                    Can402ControlwordBits.abs_rel: self.relative,
                    Can402ControlwordBits.change_set_immediately: self.immediatly
                })


        reset = partial(ChangeControlword,
                node = self.node,
                updates = {
                    Can402ControlwordBits.new_set_point: False
                })

        
        operations = [notify, reset]

        super(Notify402NewTarget, self).__init__(node, operations, *args, **kwargs)


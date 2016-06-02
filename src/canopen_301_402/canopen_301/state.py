#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flufl.enum import Enum
from canopen_301_402.constants import Can301StateCommand

class Can301State(Enum):
    initialisation  = 0
    pre_operational = 1
    operational     = 2
    stopped         = 3 # no sdo and bdo access, only nmt to change state

Can301StateTransitions = dict({
            Can301State.pre_operational: [{
                    Can301StateCommand.reset_communication: Can301State.initialisation,
                    Can301StateCommand.reset_node:          Can301State.initialisation,
                    Can301StateCommand.start_remote_node:   Can301State.operational,
                    Can301StateCommand.stop_remote_node:    Can301State.stopped
                }],
            Can301State.operational: [{
                    Can301StateCommand.reset_communication:   Can301State.initialisation,
                    Can301StateCommand.reset_node:            Can301State.initialisation,
                    Can301StateCommand.enter_pre_operational: Can301State.pre_operational,
                    Can301StateCommand.stop_remote_node:      Can301State.stopped
                }],
            Can301State.stopped: [{
                    Can301StateCommand.reset_communication:   Can301State.initialisation,
                    Can301StateCommand.reset_node:            Can301State.initialisation,
                    Can301StateCommand.enter_pre_operational: Can301State.pre_operational,
                    Can301StateCommand.start_remote_node:     Can301State.operational
                }],
        })

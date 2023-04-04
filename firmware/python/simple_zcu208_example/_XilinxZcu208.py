#-----------------------------------------------------------------------------
# This file is part of the 'Simple-ZCU208-Example'. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the 'Simple-ZCU208-Example', including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import pyrogue as pr

import axi_soc_ultra_plus_core                       as socCore
import axi_soc_ultra_plus_core.hardware.XilinxZcu208 as xilinxZcu208
import surf.xilinx                                   as xil
import simple_zcu208_example                         as rfsoc

class XilinxZcu208(pr.Device):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.add(socCore.AxiSocCore(
            offset       = 0x0000_0000,
            numDmaLanes  = 2,
            # expand       = True,
        ))

        self.add(xilinxZcu208.Hardware(
            offset       = 0x8000_0000,
            # expand       = True,
        ))

        self.add(xil.RfDataConverter(
            offset       = 0x9000_0000,
            # expand       = True,
        ))

        self.add(rfsoc.Application(
            offset       = 0xA000_0000,
            expand       = True,
        ))

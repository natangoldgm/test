###############################################################################
# Copyright (c) 2019-2020 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.
#
# All data and information contained in or disclosed by this document are
# confidential and proprietary information of Qualcomm Technologies, Inc., and
# all rights therein are expressly reserved. By accepting this material, the
# recipient agrees that this material and the information contained therein
# are held in confidence and in trust and will not be used, copied, reproduced
# in whole or in part, nor its contents revealed in any manner to others
# without the express written permission of Qualcomm Technologies, Inc.
###############################################################################

import numpy as np
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

a1 = np.fromfile(f1, dtype=np.float32)
a2 = np.fromfile(f2, dtype=np.float32)

close = np.allclose(a1, a2, atol=1e-5, rtol=1e-3)
if close:
    print("[UC_IMPL] FILES %s and %s MATCH" % (f1, f2))
else:
    print("[UC_IMPL] ERROR. MISMATCH IN %s and %s" % (f1, f2))
    print(str(a1[0]) + " " + str(a2[0]))
    print(str(a1[1]) + " " + str(a2[1]))
    print(str(a1[2]) + " " + str(a2[2]))

import numpy as np
import OpenEXR
import sys
import Imath
import array

depth = np.load(sys.argv[1])
print(depth.shape)

out = OpenEXR.OutputFile(sys.argv[2], OpenEXR.Header(depth.shape[-2], depth.shape[-1]))
out.writePixels({'R' : depth, 'G' : depth, 'B' : depth})

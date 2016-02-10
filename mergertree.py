import os, sys
import pydot
import numpy as na

if len(sys.argv) < 3:
    print "usage: %s tree_file halo_id" % sys.argv[0]
    sys.exit()

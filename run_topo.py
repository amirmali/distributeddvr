#!/usr/bin/python
# This runs the topology and executes the Bellman-Ford algorithm.
# Generically, it is run as follows:
#     python run_topo.py <topology_file> <log_file>
# For instance, to run topo1.py and log to topo1.log that we created, use the following:
#     python run_topo.py topo1 topo1.log
# Note how the topology file doesn't have the .py extension.

import sys
from Topology import *
from Node import *
from helpers import *

if len(sys.argv) != 3:
    print "Syntax:"
    print "    python run_topo.py <topology_file> <log_file>"    
    exit()

# Start up the logfile
open_log(sys.argv[2])

# Populate the topology
topo = Topology(sys.argv[1])

# Run the topology.
topo.run_topo()

# Close the logfile
finish_log()
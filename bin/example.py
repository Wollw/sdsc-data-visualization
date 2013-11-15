from mpiscope import MPIScope
from mpiscope import DummyRenderer

urlList = { "gordon"   : "http://sentinel.sdsc.edu/data/jobs/gordon"
          , "tscc"     : "http://sentinel.sdsc.edu/data/jobs/tscc"
          , "trestles" : "http://sentinel.sdsc.edu/data/jobs/trestles"
          }

mpiScope = MPIScope(DummyRenderer(), urlList)
mpiScope.run()

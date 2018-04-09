import os
try:
    os.environ["VREP"]
except KeyError:
    if os.path.exists("y:/vrep340_rev1"):
        os.environ["VREP"] = "y:/vrep340_rev1"
    else:
        raise(OSError("Can't find V-Rep share folder"))
if not os.path.exists(os.environ["VREP"]):
    raise(OSError(
        "V-Rep library directory {} does not exist!".format(
            os.environ["VREP"])))
del os
from .api import VRepApi as VRep
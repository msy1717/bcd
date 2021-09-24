# By < @Godmrunal >
# // @Botz_Official
#dont remove credit else gay

import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"BotzOfficial/plugins/{plugin_name}.py")
    name = "BotzOfficial.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["BotzOfficial.plugins." + plugin_name] = load
    print("BotzOfficial has Imported " + plugin_name)

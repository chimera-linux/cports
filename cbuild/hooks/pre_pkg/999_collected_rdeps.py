from cbuild.core import logger

import os

def invoke(pkg):
    if not os.path.isfile(pkg.destdir / "rdeps"):
        return

    with open(pkg.destdir / "rdeps") as f:
        logger.get().out_plain(f.read())

from cbuild.core import paths

import os
import shutil

def invoke(pkg):
    wrapperdir = os.path.join(paths.cbuild(), "wrappers")
    for f in os.listdir(wrapperdir):
        base, ext = os.path.splitext(f)
        if ext != ".sh":
            continue
        shutil.copy2(
            os.path.join(wrapperdir, f), pkg.statedir / "wrappers" / base
        )
        os.chmod(pkg.statedir / "wrappers" / base, 0o755)

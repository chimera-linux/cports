from cbuild.core import paths

import shutil

def invoke(pkg):
    wrapperdir = paths.cbuild() / "wrappers"
    for f in wrapperdir.iterdir():
        if f.suffix != ".sh":
            continue
        shutil.copy2(wrapperdir / f, pkg.statedir / "wrappers" / f.stem)
        (pkg.statedir / "wrappers" / f.stem).chmod(0o755)

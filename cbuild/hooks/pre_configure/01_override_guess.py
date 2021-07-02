from cbuild.core import paths

import shutil

def invoke(pkg):
    if not pkg.build_style or pkg.build_style != "gnu_configure":
        return

    for f in pkg.abs_wrksrc.rglob("*config*.*"):
        if f.is_symlink():
            continue
        if f.suffix == ".guess":
            f.unlink()
            shutil.copy(paths.cbuild() / "misc/config.guess", f)
        elif f.suffix == ".sub":
            f.unlink()
            shutil.copy(paths.cbuild() / "misc/config.sub", f)

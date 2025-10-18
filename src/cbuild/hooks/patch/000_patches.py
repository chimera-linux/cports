from cbuild.util import patch


def invoke(pkg):
    if not pkg.srcdir.is_dir():
        return
    if not pkg.patches_path.is_dir():
        return

    plist = sorted(pkg.patches_path.glob("*"))

    patch.patch(pkg, plist, stamp=True)

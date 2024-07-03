from cbuild.util import patch


def invoke(pkg):
    if not pkg.srcdir.is_dir():
        return
    if not pkg.patches_path.is_dir():
        return

    patch.patch_dir(pkg, pkg.patches_path)

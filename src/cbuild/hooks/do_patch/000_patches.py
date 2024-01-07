from cbuild.util import patch


def invoke(pkg):
    if not (pkg.builddir / pkg.wrksrc).is_dir():
        return
    if not pkg.patches_path.is_dir():
        return

    patch.patch_dir(pkg, pkg.patches_path)

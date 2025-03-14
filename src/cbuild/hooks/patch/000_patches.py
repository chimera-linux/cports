from cbuild.util import patch


def invoke(pkg):
    if not pkg.srcdir.is_dir():
        return
    if not pkg.patches_path.is_dir():
        return

    plist = sorted(pkg.patches_path.glob("*"))

    if pkg.patch_style == "git" or not pkg.patch_style:
        patch.patch_git(pkg, plist, apply_args=pkg.patch_args, stamp=True)
    elif pkg.patch_style == "patch":
        patch.patch(pkg, plist, patch_args=pkg.patch_args, stamp=True)
    else:
        pkg.error(f"invalid patch style: '{pkg.patch_style}'")

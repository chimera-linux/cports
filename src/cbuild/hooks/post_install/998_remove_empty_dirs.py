def clean_empty(pkg, dpath):
    empty = True

    for f in dpath.iterdir():
        if f.is_dir() and not f.is_symlink():
            if not clean_empty(pkg, f):
                empty = False
        else:
            empty = False

    if empty and dpath != pkg.destdir:
        pr = dpath.relative_to(pkg.destdir)
        pkg.log_warn(f"removed empty directory: {pr}")
        dpath.rmdir()
        return True

    return False


def invoke(pkg):
    if pkg.options["keepempty"]:
        return

    clean_empty(pkg, pkg.destdir)

def clean_empty(pkg, dpath):
    empty = True

    for f in dpath.iterdir():
        if f.is_dir() and not f.is_symlink():
            if not clean_empty(pkg, f):
                empty = False
        else:
            empty = False

    if empty and dpath != pkg.destdir:
        pstr = str(dpath.relative_to(pkg.destdir))
        pkg.log_warn(f"removed empty directory: {pstr}")
        dpath.rmdir()
        return True

    return False

def invoke(pkg):
    clean_empty(pkg, pkg.destdir)

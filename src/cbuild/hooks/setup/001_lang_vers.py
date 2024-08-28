from cbuild.core import paths


def invoke(pkg):
    if pkg.stage < 0:
        return
    # determine python version
    pypath = paths.bldroot() / "usr/bin/python"
    if pypath.exists():
        if not pypath.is_symlink():
            pkg.error("/usr/bin/python must be a symbolic link")
        # with proper python packaging this should always work
        pyver = pypath.readlink().name.removeprefix("python")
        if not pyver.startswith("3."):
            pkg.error(f"python version is invalid ({pyver})")
        pkg.python_major = 3
        try:
            pkg.python_minor = int(pyver[2:])
        except ValueError:
            pkg.error(f"python minor version is invalid ({pyver})")
        # can be read by templates and other things
        pkg.python_version = pyver
    else:
        pkg.python_version = None
        pkg.python_major = None
        pkg.python_minor = None
    # determine ruby version
    rbpath = paths.bldroot() / "usr/lib/ruby"
    pkg.ruby_version = None
    pkg.ruby_major = None
    pkg.ruby_minor = None
    pkg.ruby_patch = None
    if rbpath.is_dir():
        for rb in rbpath.iterdir():
            rver = rb.name.split(".")
            if len(rver) != 3:
                continue
            try:
                rmaj = int(rver[0])
                rmin = int(rver[1])
                rpatch = int(rver[2])
            except ValueError:
                continue
            pkg.ruby_version = ".".join(rver)
            pkg.ruby_major = rmaj
            pkg.ruby_minor = rmin
            pkg.ruby_patch = rpatch

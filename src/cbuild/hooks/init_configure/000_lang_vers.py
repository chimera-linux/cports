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
        pkg.python_site = None

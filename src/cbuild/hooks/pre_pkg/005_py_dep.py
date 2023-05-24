# rewrite python dependency to include version

# TODO: centralize
gpyver = "3.11"


def invoke(pkg):
    if pkg.rparent.pkgname == "python":
        return

    pyver = None

    for bc in pkg.destdir.rglob("__pycache__"):
        pkg.error("leftover unsplit pycache")

    for bc in pkg.destdir.rglob("*.py[co]"):
        pkg.error("python bytecode outside __pycache__")

    for pver in (pkg.destdir / "usr/lib").glob("python3.*"):
        if pyver:
            pkg.error("multiple python versions in package")

        pyver = pver.name.removeprefix("python")

    if not pyver:
        return

    if pyver != gpyver:
        pkg.error(f"bad python version ({pyver})")

    for i in range(0, len(pkg.depends)):
        if pkg.depends[i] == "python":
            pkg.depends[i] = f"python{pyver}~{pyver}"
            break
    else:
        # we have python stuff, add implied dependency
        pkg.depends.append(f"base-python{pyver}~{pyver}")

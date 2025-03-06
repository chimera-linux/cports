# rewrite python dependency to include version


def invoke(pkg):
    if pkg.rparent.pkgname == "python" or pkg.autopkg:
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

    if pyver != pkg.rparent.python_version:
        pkg.error(f"bad python version ({pyver})")

    # other python versions
    if pkg.rparent.pkgname == f"python{pyver}":
        return

    for i in range(0, len(pkg.install_if)):
        if pkg.install_if[i] == "python-pycache":
            pkg.install_if[i] = f"python-pycache~{pyver}"
            break

    for i in range(0, len(pkg.depends)):
        if pkg.depends[i] == "python":
            pkg.depends[i] = f"python{pyver}"
            break
    else:
        # we have python stuff, add implied dependency
        pkg.depends.append(f"python-python{pyver}-meta")

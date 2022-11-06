# rewrite python dependency to include version

def invoke(pkg):
    pyver = None

    for pver in (pkg.destdir / "usr/lib").glob("python3.*"):
        pyver = pver.name.removeprefix("python")
        break
    else:
        return

    for i in range(0, len(pkg.depends)):
        if pkg.depends[i] == "python":
            pkg.depends[i] = f"python~{pyver}"
            return

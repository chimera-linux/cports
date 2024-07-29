def invoke(pkg):
    bpkg = pkg.rparent

    # subpackages only
    if bpkg == pkg or pkg.autopkg:
        return

    # we let packages define their own
    if len(pkg.install_if) > 0 or not pkg.options["scandevelif"]:
        return

    # devel packages only
    if not pkg.pkgname.endswith("-devel"):
        return

    # special case
    if pkg.pkgname == "base-devel":
        return

    pv = f"{bpkg.pkgver}-r{bpkg.pkgrel}"

    matchdeps = {f"{bpkg.pkgname}={pv}": True}

    for sp in pkg.rparent.subpkg_list:
        if sp == pkg:
            continue
        matchdeps[f"{sp.pkgname}={pv}"] = True

    iif = []

    for dep in pkg.depends:
        if dep in matchdeps:
            iif.append(dep)

    if len(iif) == 0:
        return

    iif.append("base-devel")
    pkg.install_if = iif

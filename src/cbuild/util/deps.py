def collect_deps(pkg):
    # dependencies of any sort
    deps = []

    # bootstrap packages are not installable ootb
    if pkg.pkgname.endswith("-bootstrap") and pkg.build_style != "meta":
        deps += ["bootstrap:" + pkg.pkgname.removesuffix("-bootstrap")]

    # explicit package depends
    for c in pkg.depends:
        ploc = c.find("!")
        if ploc > 0:
            deps.append(c[0:ploc].removeprefix("virtual:"))
        else:
            deps.append(c.removeprefix("virtual:"))

    # sort before adding more
    deps.sort()

    # shlib requires
    if hasattr(pkg, "so_requires"):
        deps += map(lambda v: f"so:{v}", sorted(pkg.so_requires))

    # .pc file requires
    if hasattr(pkg, "pc_requires"):
        deps += map(lambda v: f"pc:{v}", sorted(pkg.pc_requires))

    return deps

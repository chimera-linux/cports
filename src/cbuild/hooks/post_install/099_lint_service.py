from cbuild.core.chroot import host_path_to_chroot


def invoke(pkg):
    # we skip dinitcheck on base-cbuild until we're done bootstrapping
    if pkg.stage < 2:
        return

    syspath = "etc/dinit.d"
    userpath = "etc/dinit.d/user"

    dservicepaths = []

    if (dsyspath := pkg.destdir / syspath).is_dir():
        dservicepaths.extend(dsyspath.iterdir())
    if (duserpath := pkg.destdir / userpath).is_dir():
        dservicepaths.extend(duserpath.iterdir())

    for dservicepath in dservicepaths:
        if dservicepath.is_dir() or dservicepath.is_symlink():
            continue
        cdservicepath = host_path_to_chroot(dservicepath)
        pkg.do(
            "dinitcheck",
            "--user" if cdservicepath.parent.name == "user" else "--system",
            "--services-dir",
            cdservicepath.parent,
            cdservicepath.name,
        )

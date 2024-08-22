# include trigger autodeps
#
# some stuff should always have a dependency on the package
# it triggers, particularly stuff like sysusers/tmpfiles
#
# TODO: maybe figure out a way to decentralize this?

from cbuild.core import logger

_trigdeps = {
    "etc/ca-certificates/update.d": "ca-certificates",
    "usr/share/ca-certificates": "ca-certificates",
}


def invoke(pkg):
    if not pkg.options["scantrigdeps"] or pkg.autopkg:
        return

    deps = []
    log = logger.get()

    for key in _trigdeps:
        if (pkg.destdir / key).is_dir():
            pkgn = _trigdeps[key]
            # don't add self-dependency
            if pkg.pkgname == pkgn:
                continue
            deps.append((key, pkgn))

    depl = list(filter(lambda tpl: tpl[1] not in pkg.depends, deps))

    depset = set()
    for path, dep in depl:
        log.out_plain(f"  \f[cyan]TRIGGER DEPENDENCY:\f[] {path} -> {dep}")
        # add it only once in case several paths add the same dep
        if dep not in depset:
            pkg.depends.append(dep)
            depset.add(dep)

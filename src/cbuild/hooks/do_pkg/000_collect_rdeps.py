from cbuild.core import logger
from cbuild.apk import cli
from cbuild.util.deps import collect_deps


def invoke(pkg):
    pkg.all_rdeps = collect_deps(pkg)

    subp = cli.call_chroot(
        "info", ["--depends", "--", pkg.pkgname], pkg, capture_output=True
    )

    log = logger.get()

    if subp.returncode != 0:
        log.warn(f'Could not get original dependencies of "{pkg.pkgname}"')
        return

    log.out("Dependency comparison between original and newly-built package:")

    # first line is e.g. "foo-1.0.0-r0 depends on:", so skip it
    orig_rdeps = subp.stdout.decode().strip().split("\n\n")[0].split("\n")[1:]

    list1s = set(orig_rdeps)
    list2s = set(pkg.all_rdeps)

    lists = set(list1s)
    lists.update(list2s)

    for v in sorted(lists):
        if v in list1s:
            if v not in list2s:
                log.out_red(f"-{v}")
                continue
        else:
            if v in list2s:
                log.out_green(f"+{v}")
                continue
        log.out(f" {v}")

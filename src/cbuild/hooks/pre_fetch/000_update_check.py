from cbuild.core import update_check


def invoke(pkg):
    if not pkg.update_check:
        return

    cv = update_check.update_check(pkg, False, True)
    if cv is None:
        pkg.error("no versions found, broken update-check?")

    for pv, nv in cv:
        pkg.log_warn(f"update available: {pv} -> {nv}")

    if cv:
        pkg.error("updates found, aborting")

from cbuild.core import template, dependencies, scanelf

import shutil


def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)


def _invoke_subpkg(pkg):
    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)
    if pkg.pkg_install:
        template.call_pkg_hooks(pkg, "pre_install")
        template.run_pkg_func(pkg, "pkg_install", on_subpkg=True)
    # get own licenses by default
    pkg.take(f"usr/share/licenses/{pkg.pkgname}", missing_ok=True)


def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done"

    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    template.call_pkg_hooks(pkg, "init_install")
    template.run_pkg_func(pkg, "init_install")

    if install_done.is_file() and (not pkg.force_mode or step != "install"):
        # when repeating, ensure to at least scan the ELF info...
        for sp in pkg.subpkg_list:
            scanelf.scan(sp, pkg.current_elfs)
        scanelf.scan(pkg, pkg.current_elfs)
        return

    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)
    pkg.run_step("install", skip_post=True)

    pkg.install_done = True

    for sp in pkg.subpkg_list:
        _invoke_subpkg(sp)
        scanelf.scan(sp, pkg.current_elfs)
        template.call_pkg_hooks(sp, "post_install")

    scanelf.scan(pkg, pkg.current_elfs)
    template.call_pkg_hooks(pkg, "post_install")

    install_done.touch()

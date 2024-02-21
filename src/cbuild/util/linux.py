# linux kernel packaging helpers


def get_arch(arch):
    match arch:
        case "ppc64le" | "ppc64" | "ppc":
            return "powerpc"
        case "aarch64":
            return "arm64"
        case "x86_64":
            return "x86_64"
        case "riscv64":
            return "riscv"
        case _:
            # unknown, fill in
            return None


def _gen_script(pkg, script, flavor, args=""):
    pkg.scriptlets[script] = (
        f'/usr/libexec/base-kernel/script-{script} "$1"{args} "{flavor}"'
    )


def generate_scriptlets(pkg, flavor):
    # generate scriptlets for packaging, just hooking to base-kernel helpers
    _gen_script(pkg, "pre-install", flavor)
    _gen_script(pkg, "pre-upgrade", flavor, ' "$2"')
    _gen_script(pkg, "pre-deinstall", flavor)
    _gen_script(pkg, "post-install", flavor)
    _gen_script(pkg, "post-upgrade", flavor, ' "$2"')


def _build_env(pkg, menv, base_env, env):
    renv = dict(menv)
    # needed for efistub
    renv["CBUILD_BYPASS_STRIP_WRAPPER"] = "1"
    if base_env:
        renv.update(base_env)
    if env:
        renv.update(env)
    return renv


def configure(pkg, flavor, build_dir=None, env=None):
    cfgarch = pkg.profile().arch
    cfgname = f"config-{cfgarch}.{flavor}"

    pkg.cp(pkg.files_path / cfgname, pkg.cwd)

    epoch = pkg.source_date_epoch or 0
    args = []

    if pkg.profile().cross:
        args += [f"CROSS_COMPILE={pkg.profile().triplet}"]

    bdir = build_dir
    if not bdir:
        bdir = pkg.make_dir

    pkg.do(
        "chimera-buildkernel",
        "prepare",
        f"ARCH={get_arch(cfgarch)}",
        f"CONFIG_FILE={pkg.chroot_cwd}/{cfgname}",
        f"OBJDIR={bdir}",
        f"JOBS={pkg.make_jobs}",
        f"LOCALVERSION=-{pkg.pkgrel}-{flavor}",
        f"EPOCH={epoch}",
        *args,
        env=_build_env(pkg, pkg.configure_env, None, env),
    )


def update_configs(pkg, archs, flavor):
    for a in archs:
        with pkg.profile(a):
            with pkg.stamp(f"{a}_config"):
                pkg.log(f"configuring {a}...")
                configure(pkg, flavor, f"{pkg.make_dir}-{a}")
                pkg.log("now perform other config (press enter once done)")
                input()
                pkg.cp(
                    f"{pkg.make_dir}-{a}/.config",
                    pkg.files_path / f"config-{a}.{flavor}",
                )
    pkg.error("kernel configs have been updated")


def build(pkg, flavor, env=None):
    pkg.do(
        "chimera-buildkernel",
        "build",
        env=_build_env(pkg, pkg.make_env, pkg.make_build_env, env),
    )


def install(pkg, flavor, env=None):
    pkg.do(
        "chimera-buildkernel",
        "install",
        pkg.chroot_destdir,
        env=_build_env(pkg, pkg.make_env, pkg.make_install_env, env),
    )
    kpath = f"usr/lib/modules/{pkg.pkgver}-{pkg.pkgrel}-{flavor}"
    # mutable files go to a separate dist directory, to be handled by hooks
    pkg.install_dir(f"{kpath}/apk-dist")
    for f in (pkg.destdir / kpath).glob("modules.*"):
        pkg.mv(f, f.parent / "apk-dist")


# api to manipulate out of tree modules


def get_version(pkg, expected=None):
    from cbuild.core import paths

    kver = None
    for f in (paths.bldroot() / "usr/lib/modules").iterdir():
        if kver:
            pkg.error(f"kernel version already set: {kver}")
        kver = f.name

    if expected and expected not in kver:
        pkg.error(f"kernel mismatch: {kver} (expected {expected})")

    return kver


def get_modsrc(pkg, modname, modver):
    from cbuild.core import paths

    return paths.bldroot() / f"usr/src/{modname}-{modver}"


def generate_scriptlets_ckms(pkg, modname, kernver):
    prescript = f"""rm -f /boot/initramfs-{kernver}.img || :
rm -f /boot/initrd.img-{kernver} || :"""

    postscript = f"""if [ -f /boot/System.map-{kernver} ]; then
    depmod -a -F /boot/System.map-{kernver} {kernver} || :
else
    depmod -a {kernver} || :
fi"""

    pkg.scriptlets["pre-install"] = (
        prescript
        + f"""
if [ -x /usr/bin/ckms ]; then
    ckms -q -k {kernver} uninstall {modname} > /dev/null 2>&1 || :
fi"""
    )
    pkg.scriptlets["pre-upgrade"] = prescript
    pkg.scriptlets["pre-deinstall"] = prescript
    pkg.scriptlets["post-install"] = postscript
    pkg.scriptlets["post-upgrade"] = postscript
    pkg.scriptlets["post-deinstall"] = postscript


def _call_ckms(pkg, kver, *args):
    pkg.do(
        "ckms",
        "-s",
        pkg.chroot_cwd,
        "-k",
        kver,
        *args,
        env={"CBUILD_BYPASS_STRIP_WRAPPER": "1"},
    )


def ckms_configure(pkg, modname, modver, kver):
    _call_ckms(pkg, kver, "add", f"/usr/src/{modname}-{modver}")


def ckms_build(pkg, modname, modver, kver):
    _call_ckms(pkg, kver, "build", f"{modname}={modver}")


def ckms_install(pkg, modname, modver, kver):
    modbase = "usr/lib/modules"
    moddest = f"{modbase}/{kver}"

    pkg.install_dir(moddest)
    _call_ckms(
        pkg,
        kver,
        "-d",
        pkg.chroot_destdir / modbase,
        "-D",
        "-x",
        "zst",
        "install",
        f"{modname}={modver}",
    )

    cdpath = f"{moddest}/ckms-disable/{modname}"
    pkg.install_dir(cdpath)
    (pkg.destdir / cdpath / modver).touch(0o644)

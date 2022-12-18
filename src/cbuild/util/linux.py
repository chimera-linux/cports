# linux kernel packaging helpers

def get_arch(arch):
    match arch:
        case "ppc64le" | "ppc64":
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

def _gen_script(pkg, script, flavor, args = ""):
    pkg.scriptlets[script] = f'/usr/libexec/base-kernel/script-{script} "$1"{args} "{flavor}"'

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

def configure(pkg, flavor, env = None):
    cfgarch = pkg.profile().arch
    cfgname = f"config-{cfgarch}.{flavor}"

    pkg.cp(pkg.files_path / cfgname, pkg.cwd)

    epoch = pkg.source_date_epoch or 0
    args = []

    if pkg.profile().cross:
        args += [f"CROSS_COMPILE={pkg.profile().triplet}"]

    pkg.do(
        "chimera-buildkernel",
        "prepare",
        f"ARCH={get_arch(cfgarch)}",
        f"CONFIG_FILE={pkg.chroot_cwd}/{cfgname}",
        f"OBJDIR={pkg.make_dir}",
        f"JOBS={pkg.make_jobs}",
        f"LOCALVERSION=-{pkg.pkgrel}-{flavor}",
        f"EPOCH={epoch}",
        *args,
        env = _build_env(pkg, pkg.configure_env, None, env)
    )

def build(pkg, flavor, env = None):
    pkg.do(
        "chimera-buildkernel", "build",
        env = _build_env(pkg, pkg.make_env, pkg.make_build_env, env)
    )

def install(pkg, flavor, env = None):
    pkg.do(
        "chimera-buildkernel", "install", pkg.chroot_destdir,
        env = _build_env(pkg, pkg.make_env, pkg.make_install_env, env)
    )
    kpath = f"usr/lib/modules/{pkg.pkgver}-{pkg.pkgrel}-{flavor}"
    # mutable files go to a separate dist directory, to be handled by hooks
    pkg.install_dir(f"{kpath}/apk-dist")
    for f in (pkg.destdir / kpath).glob("modules.*"):
        pkg.mv(f, f.parent / "apk-dist")

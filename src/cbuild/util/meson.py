def _make_crossfile(pkg, build_dir):
    if not pkg.profile().cross:
        return

    cfpath = pkg.cwd / build_dir / "cbuild.cross"

    (pkg.cwd / build_dir).mkdir(parents=True, exist_ok=True)

    # map known profiles to meson arch
    match pkg.profile().arch:
        case "aarch64" | "x86_64" | "riscv64":
            meson_cpu = pkg.profile().arch
        case "ppc64le" | "ppc64":
            meson_cpu = "ppc64"
        case "ppc":
            meson_cpu = "ppc"
        case "armhf" | "armv7":
            meson_cpu = "arm"
        case _:
            pkg.error(f"unknown meson architecture: {pkg.profile().arch}")

    with open(cfpath, "w") as outf:
        outf.write(
            f"""
[binaries]
c = '{pkg.get_tool("CC")}'
cpp = '{pkg.get_tool("CXX")}'
ar = '{pkg.get_tool("AR")}'
nm = '{pkg.get_tool("NM")}'
ld = '{pkg.get_tool("LD")}'
strip = '{pkg.get_tool("STRIP")}'
readelf = '{pkg.get_tool("READELF")}'
objcopy = '{pkg.get_tool("OBJCOPY")}'
pkgconfig = '{pkg.get_tool("PKG_CONFIG")}'
llvm-config = '/usr/bin/llvm-config'
rust = ['rustc', '--target', '{pkg.profile().triplet}', '--sysroot', '{pkg.profile().sysroot / "usr"}']

[properties]
needs_exe_wrapper = true

[built-in options]
c_args = {pkg.get_cflags()}
c_link_args = {pkg.get_ldflags()}

cpp_args = {pkg.get_cxxflags()}
cpp_link_args = {pkg.get_ldflags()}

[host_machine]
system = 'linux'
cpu_family = '{meson_cpu}'
cpu = '{pkg.profile().arch}'
endian = '{pkg.profile().endian}'
"""
        )

    return cfpath


def configure(pkg, build_dir, meson_dir=None, extra_args=[], env={}):
    if not meson_dir:
        meson_dir = "."

    cfp = _make_crossfile(pkg, build_dir)

    cargs = []
    if cfp:
        cargs = [
            "--cross-file=" + str(pkg.chroot_cwd / cfp.relative_to(pkg.cwd))
        ]

    if pkg.has_lto():
        cargs.append("-Db_lto=true")
        # mode, thin is default for us
        if pkg.options["ltofull"]:
            cargs.append("-Db_lto_mode=default")
        else:
            cargs.append("-Db_lto_mode=thin")
    else:
        cargs.append("-Db_lto=false")

    pkg.do(
        "meson",
        "setup",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--libexecdir=/usr/libexec",
        "--bindir=/usr/bin",
        "--sbindir=/usr/bin",
        "--includedir=/usr/include",
        "--datadir=/usr/share",
        "--mandir=/usr/share/man",
        "--infodir=/usr/share/info",
        "--sysconfdir=/etc",
        "--localstatedir=/var",
        "--sharedstatedir=/var/lib",
        "--buildtype=plain",
        "--auto-features=auto",
        "--wrap-mode=nodownload",
        "-Ddefault_library=both",
        "-Dwerror=false",
        "-Db_staticpic=true",
        "-Dpkgconfig.relocatable=false",
        "-Dpython.bytecompile=0",
        *cargs,
        *extra_args,
        meson_dir,
        build_dir,
        env=env,
    )


def invoke(pkg, command, build_dir, extra_args=[], env={}, wrapper=[]):
    pkg.do(
        *wrapper,
        "meson",
        command,
        *extra_args,
        wrksrc=build_dir,
        env=env,
    )


def install(pkg, build_dir, extra_args=[], env={}, wrapper=[]):
    renv = {"DESTDIR": str(pkg.chroot_destdir)}
    renv.update(env)
    invoke(
        pkg, "install", build_dir, ["--no-rebuild", *extra_args], renv, wrapper
    )


def test(pkg, build_dir, extra_args=[], env={}, wrapper=[]):
    invoke(
        pkg,
        "test",
        build_dir,
        [
            "--no-rebuild",
            "--print-errorlogs",
            "--num-processes",
            str(pkg.make_jobs),
            *extra_args,
        ],
        env,
        wrapper,
    )

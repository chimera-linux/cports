from cbuild.core import paths

def _make_crossfile(pkg, build_dir):
    if not pkg.build_profile.cross:
        return

    cfpath = pkg.cwd / build_dir / "cbuild.cross"

    (pkg.cwd / build_dir).mkdir(parents = True, exist_ok = True)

    # map known profiles to meson arch
    match pkg.build_profile.arch:
        case "aarch64" | "x86_64" | "riscv64":
            meson_cpu = pkg.build_profile.arch
        case "ppc64le" | "ppc64":
            meson_cpu = "ppc64"
        case _:
            pkg.error(f"unknown architecture: {pkg.build_profile.arch}")

    with open(cfpath, "w") as outf:
        outf.write(f"""
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
cpu = '{pkg.build_profile.arch}'
endian = '{pkg.build_profile.endian}'
""")

    return cfpath

def configure(pkg, meson_dir = None, build_dir = None, extra_args = []):
    if not meson_dir:
        meson_dir = "."

    if not build_dir:
        build_dir = pkg.make_dir

    cfp = _make_crossfile(pkg, build_dir)

    cargs = []
    if cfp:
        cargs = ["--cross-file=" + str(
            pkg.chroot_cwd / cfp.relative_to(pkg.cwd)
        )]

    pkg.do(
        "meson", [
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
            "-Db_ndebug=true",
            "-Db_staticpic=true"
        ] + cargs + pkg.configure_args + extra_args + [meson_dir, build_dir]
    )

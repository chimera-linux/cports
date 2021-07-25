from cbuild.core import paths

def _make_crossfile(pkg, build_dir):
    if not pkg.build_profile.cross:
        return

    cfpath = pkg.abs_build_wrksrc / build_dir / "cbuild.cross"

    (pkg.abs_build_wrksrc / build_dir).mkdir(parents = True, exist_ok = True)

    # map known profiles to meson arch
    meson_cpu = {
        "aarch64": "aarch64",
        "ppc64le": "ppc64",
        "ppc64": "ppc64",
        "x86_64": "x86_64",
        "riscv64": "riscv64"
    }.get(pkg.build_profile.arch, None)

    if not meson_cpu:
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
c_args = {str(pkg.get_cflags())}
c_link_args = {str(pkg.get_ldflags())}

cpp_args = {str(pkg.get_cxxflags())}
cpp_link_args = {str(pkg.get_ldflags())}

[host_machine]
system = 'linux'
cpu_family = '{meson_cpu}'
cpu = '{pkg.build_profile.arch}'
endian = '{pkg.build_profile.endian}'
""")

    return cfpath

def configure(pkg, meson_dir = None, build_dir = "build", extra_args = []):
    if not meson_dir:
        meson_dir = "."

    cfp = _make_crossfile(pkg, build_dir)

    cargs = []
    if cfp:
        cargs = ["--cross-file=" + str(
            pkg.chroot_build_wrksrc / cfp.relative_to(pkg.abs_build_wrksrc)
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
        ] + cargs + pkg.configure_args + extra_args + [meson_dir, build_dir],
        build = True
    )

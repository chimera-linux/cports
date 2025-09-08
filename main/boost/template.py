pkgname = "boost"
pkgver = "1.89.0"
pkgrel = 0
hostmakedepends = ["pkgconf", "python"]
makedepends = [
    "bzip2-devel",
    "icu-devel",
    "linux-headers",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
provides = [self.with_pkgver(f"boost{pkgver[:-2]}")]
pkgdesc = "Free peer-reviewed portable C++ source libraries"
license = "BSL-1.0"
url = "https://boost.org"
source = f"https://archives.boost.io/release/{pkgver}/source/boost_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "9de758db755e8330a01d995b0a24d09798048400ac25c03fc5ea9be364b13c93"
options = ["empty"]

# libs have semi-auto-generated subpkgs using this array
# needs to be updated with new libs regularly
_libs = [
    "atomic",
    "charconv",
    "chrono",
    "container",
    "context",
    "contract",
    "coroutine",
    "date_time",
    "fiber",
    "filesystem",
    "graph",
    "iostreams",
    "json",
    "locale",
    "log_setup",
    "log",
    "math",
    "nowide",
    "prg_exec_monitor",
    "process",
    "program_options",
    "python",
    "random",
    "regex",
    "serialization",
    "stacktrace_addr2line",
    "stacktrace_basic",
    "stacktrace_noop",
    "thread",
    "timer",
    "type_erasure",
    "unit_test_framework",
    "url",
    "wave",
    "wserialization",
]

match self.profile().arch:
    case "ppc64le" | "ppc64" | "ppc":
        _arch, _abi = "power", "sysv"
    case "aarch64" | "armhf" | "armv7":
        _arch, _abi = "arm", "aapcs"
    case "x86_64":
        _arch, _abi = "x86", "sysv"
        _libs.append("stacktrace_from_exception")
    case "loongarch64":
        _arch, _abi = "loongarch", "sysv"
    case "riscv64":
        _arch, _abi = "riscv", "sysv"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def _call_b2(self, *args):
    self.do(
        self.chroot_cwd / "b2",
        f"-j{self.make_jobs}",
        f"--user-config={self.chroot_cwd}/user-config.jam",
        f"--prefix={self.chroot_destdir}/usr",
        "release",
        f"python={self.python_version}",
        f"architecture={_arch}",
        f"abi={_abi}",
        "toolset=clang",
        "cxxflags=" + self.get_cxxflags(shell=True),
        "linkflags=" + self.get_ldflags(shell=True),
        "threading=multi",
        "debug-symbols=off",
        "runtime-link=shared",
        "link=shared,static",
        "--layout=system",
        *args,
    )


def build(self):
    self.do(
        self.chroot_cwd / "bootstrap.sh",
        f"--prefix={self.chroot_destdir}/usr",
        "--with-python=/usr/bin/python",
        "--with-python-root=/usr",
        # runs windres on res.rc and tries to link in a COFF object otherwise
        # which clang rejects
        env={"B2_DONT_EMBED_MANIFEST": "1"},
    )

    with open(self.cwd / "user-config.jam", "w") as cf:
        cf.write(
            f"""
using clang : : {self.get_tool("CXX")} : <cxxflags>"{self.get_cxxflags(shell=True)}" <linkflags>"{self.get_ldflags(shell=True)}" <warnings-as-errors>"off" ;
using python : {self.python_version} : /usr/bin/python3 : {self.profile().sysroot}/usr/include/python{self.python_version} : {self.profile().sysroot}/usr/lib/python{self.python_version} ;
"""
        )

    _call_b2(self)

    if self.profile().cross:
        # build b2 again, this time for the target system
        self.do(
            self.chroot_cwd / "tools/build/src/engine/build.sh",
            "--cxx=" + self.get_tool("CXX"),
            "--cxxflags=" + self.get_cxxflags(shell=True),
            "clang",
            env={"B2_DONT_EMBED_MANIFEST": "1"},
        )


def check(self):
    self.do(
        "python",
        "test_all.py",
        "--default-bjam",
        wrksrc="tools/build/test",
        env={"PATH": f"{self.chroot_cwd}/tools/build/src/engine:/usr/bin"},
    )


def install(self):
    # install b2 globally
    self.install_bin("tools/build/src/engine/b2")

    # install boost itself
    _call_b2(self, "install")

    # install Boost.Build files
    self.install_dir("usr/share/b2")

    for f in (self.cwd / "tools/build").glob("*"):
        self.cp(f, self.destdir / "usr/share/b2", recursive=True)

    for f in (self.destdir / "usr/share/b2").rglob("*.orig"):
        f.unlink()

    self.uninstall("usr/share/b2/src/engine/b2")

    self.install_dir("etc")

    with open(self.destdir / "etc/site-config.jam", "w") as sc:
        sc.write(
            """# System-wide configuration file for Boost.Build.

using clang ;
"""
        )

    self.install_license("LICENSE_1_0.txt")


@subpackage("boost-build")
def _(self):
    self.subdesc = "Boost.Build framework"
    self.depends = [self.parent]
    self.provides = [self.with_pkgver(f"boost{pkgver[:-2]}-build")]

    return ["usr/bin/b2", "etc/site-config.jam", "usr/share/b2"]


@subpackage("boost-devel")
def _(self):
    self.depends = [self.parent, *makedepends]
    self.provides = [self.with_pkgver(f"boost{pkgver[:-2]}-devel")]

    return self.default_devel(extra=["usr/share/boost_predef"])


def _gen_libp(libname):
    @subpackage(f"boost-{libname}-libs")
    def _(self):
        self.subdesc = libname
        self.depends = [self.parent]
        self.provides = [self.with_pkgver(f"libboost_{libname}")]

        return [f"usr/lib/libboost_{libname}*.so.*"]


for _blib in _libs:
    _gen_libp(_blib)

pkgname = "boost"
pkgver = "1.85.0"
pkgrel = 3
hostmakedepends = ["pkgconf"]
makedepends = [
    "bzip2-devel",
    "icu-devel",
    "linux-headers",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
provides = [f"boost{pkgver[:-2]}={pkgver}-r{pkgrel}"]
pkgdesc = "Free peer-reviewed portable C++ source libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSL-1.0"
url = "https://boost.org"
source = f"https://boostorg.jfrog.io/artifactory/main/release/{pkgver}/source/boost_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "be0d91732d5b0cc6fbb275c7939974457e79b54d6f07ce2e3dfdd68bef883b0b"
tool_flags = {"CXXFLAGS": ["-std=c++14"]}
# FIXME: odd failures, but seems test-related
options = ["!check", "!cross", "empty"]  # i don't dare touch this yet

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
    "program_options",
    "python",
    "random",
    "regex",
    "serialization",
    "stacktrace_addr2line",
    "stacktrace_basic",
    "stacktrace_noop",
    "system",
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
    case "aarch64":
        _arch, _abi = "arm", "aapcs"
    case "x86_64":
        _arch, _abi = "x86", "sysv"
    case "riscv64":
        _arch, _abi = "riscv", "sysv"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def init_configure(self):
    self._pyver = (
        self.do("pkgconf", "--modversion", "python3", capture_output=True)
        .stdout.decode()
        .strip()
    )


def _call_b2(self, *args):
    self.do(
        self.chroot_cwd / "b2",
        f"-j{self.make_jobs}",
        f"--user-config={self.chroot_cwd}/user-config.jam",
        f"--prefix={self.chroot_destdir}/usr",
        "release",
        f"python={self._pyver}",
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


def do_build(self):
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
using python : {self._pyver} : /usr/bin/python3 : /usr/include/python{self._pyver} : /usr/lib/python{self._pyver} ;
"""
        )

    _call_b2(self)


def do_install(self):
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


def do_check(self):
    self.do(
        "python",
        "test_all.py",
        "--default-bjam",
        wrksrc="tools/build/test",
        env={"PATH": f"{self.chroot_cwd}/tools/build/src/engine:/usr/bin"},
    )


@subpackage("boost-build")
def _jam(self):
    self.pkgdesc = f"{pkgdesc} (Boost.Build framework)"
    self.depends = [f"boost={pkgver}-r{pkgrel}"]
    self.provides = [f"boost{pkgver[:-2]}-build={pkgver}-r{pkgrel}"]

    return ["usr/bin/b2", "etc/site-config.jam", "usr/share/b2"]


@subpackage("boost-devel")
def _devel(self):
    self.depends = [f"boost={pkgver}-r{pkgrel}"] + makedepends
    self.provides = [f"boost{pkgver[:-2]}-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()


def _gen_libp(libname):
    @subpackage(f"boost-{libname}-libs")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({libname})"
        self.depends = [f"boost={pkgver}-r{pkgrel}"]
        self.provides = [f"libboost_{libname}={pkgver}-r{pkgrel}"]

        return [f"usr/lib/libboost_{libname}*.so.*"]


for _blib in _libs:
    _gen_libp(_blib)

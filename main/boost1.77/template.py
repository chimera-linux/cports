pkgname = "boost1.77"
pkgver = "1.77.0"
pkgrel = 0
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "libbz2-devel", "liblzma-devel", "libzstd-devel",
    "icu-devel", "python-devel", "linux-headers"
]
pkgdesc = "Free peer-reviewed portable C++ source libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSL-1.0"
url = "https://boost.org"
source = f"https://boostorg.jfrog.io/artifactory/main/release/{pkgver}/source/boost_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "5347464af5b14ac54bb945dc68f1dd7c56f0dad7262816b956138fc53bcc0131"
tool_flags = {"CXXFLAGS": ["-std=c++14"]}
options = ["!cross"] # i don't dare touch this yet

_bver = pkgver[:-2]

# libs have semi-auto-generated subpkgs using this array
# needs to be updated with new libs regularly
_libs = [
    "atomic", "chrono", "container", "context", "contract", "coroutine",
    "date_time", "fiber", "filesystem", "graph", "iostreams", "json", "locale",
    "log_setup", "log", "math", "nowide", "prg_exec_monitor", "program_options",
    "python", "random", "regex", "serialization", "stacktrace_addr2line",
    "stacktrace_basic", "stacktrace_noop", "system", "thread", "timer",
    "type_erasure", "unit_test_framework", "wave", "wserialization",
]

match self.profile().arch:
    case "ppc64le" | "ppc64":
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
    self._pyver = self.do(
        "pkgconf", "--modversion", "python3", capture_output = True
    ).stdout.decode().strip()

def _call_b2(self, *args):
    self.do(
        self.chroot_cwd / "b2", f"-j{self.make_jobs}",
        f"--user-config={self.chroot_cwd}/user-config.jam",
        f"--prefix={self.chroot_destdir}/usr",
        "release",
        f"python={self._pyver}",
        "toolset=clang",
        "threading=multi",
        "debug-symbols=off",
        "runtime-link=shared",
        "link=shared,static",
        "--layout=system",
        *args
    )

def do_build(self):
    self.do(
        self.chroot_cwd / "bootstrap.sh",
        f"--prefix={self.chroot_destdir}/usr",
        f"--with-python=/usr/bin/python",
        f"--with-python-root=/usr"
    )

    with open(self.cwd / "user-config.jam", "w") as cf:
        cf.write(f"""
using clang : : {self.get_tool("CXX")} : <cxxflags>"{self.get_cxxflags(shell = True)}" <linkflags>"{self.get_ldflags(shell = True)}" ;
using python : {self._pyver} : /usr/bin/python3 : /usr/include/python{self._pyver} : /usr/lib/python{self._pyver} ;
""")

    _call_b2(self)

def do_install(self):
    # install bjam globally
    self.install_bin("tools/build/src/engine/bjam")
    self.install_bin("tools/build/src/engine/b2")

    # install boost itself
    _call_b2(self, "install")

    # install Boost.Build files
    self.install_dir("usr/share/boost-build")

    for f in (self.cwd / "tools/build").glob("*"):
        self.cp(f, self.destdir / "usr/share/boost-build", recursive = True)

    for f in (self.destdir / "usr/share/boost-build").rglob("*.orig"):
        f.unlink()

    self.rm(self.destdir / "usr/share/boost-build/src/engine/b2")
    self.rm(self.destdir / "usr/share/boost-build/src/engine/bjam")

    self.install_dir("etc")

    with open(self.destdir / "etc/site-config.jam", "w") as sc:
        sc.write("""# System-wide configuration file for Boost.Build.

using clang ;
""")

    self.install_license("LICENSE_1_0.txt")

def do_check(self):
    self.do(
        "python", "test_all.py", "--default-bjam",
        wrksrc = "tools/build/test",
        env = {
            "PATH": f"{self.chroot_cwd}/tools/build/src/engine:/usr/bin"
        }
    )

@subpackage(f"boost{_bver}-build")
def _jam(self):
    self.pkgdesc = f"{pkgdesc} (Boost.Build framework)"
    self.depends = [f"boost{_bver}={pkgver}-r{pkgrel}"]
    self.provides = [f"boost-build={pkgver}-r{pkgrel}"]

    return ["etc/site-config.jam", "usr/share/boost-build"]

@subpackage(f"boost{_bver}-jam")
def _jam(self):
    self.pkgdesc = f"{pkgdesc} (bjam utility)"
    self.depends = [f"boost{_bver}-build={pkgver}-r{pkgrel}"]
    self.provides = [f"boost-jam={pkgver}-r{pkgrel}"]

    return ["usr/bin/bjam", "usr/bin/b2"]

@subpackage(f"boost{_bver}-devel")
def _devel(self):
    self.depends = [f"boost{_bver}={pkgver}-r{pkgrel}"] + makedepends

    return self.default_devel()

# this exists so things can easily makedepend on it
# otherwise i would have done a virtual here as well
@subpackage("boost-devel")
def _develmeta(self):
    self.depends = [f"boost{_bver}-devel={pkgver}-r{pkgrel}"]
    self.build_style = "meta"

    return []

def _gen_libp(libname):
    @subpackage(f"libboost_{libname}{_bver}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({libname})"
        self.depends = [f"boost{_bver}={pkgver}-r{pkgrel}"]
        self.provides = [f"libboost_{libname}={pkgver}-r{pkgrel}"]

        return [f"usr/lib/libboost_{libname}*.so.*"]

for blib in _libs:
    _gen_libp(blib)

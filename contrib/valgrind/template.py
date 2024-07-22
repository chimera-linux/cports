pkgname = "valgrind"
pkgver = "3.23.0"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "ppc", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--without-mpicc"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."  # junk in main dir prevents reliable out of tree build
hostmakedepends = [
    "automake",
    "gmake",
    "gsed",
    "libtool",
    "perl",
    "pkgconf",
]
makedepends = ["libomp-devel", "linux-headers"]
depends = ["perl", "python"]
pkgdesc = "Instrumentation framework for building dynamic analysis tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://valgrind.org"
source = f"https://sourceware.org/pub/valgrind/valgrind-{pkgver}.tar.bz2"
sha256 = "c5c34a3380457b9b75606df890102e7df2c702b9420c2ebef9540f8b5d56264d"
debug_level = 1
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE", "-fPIC"], "LDFLAGS": ["-fPIC"]}
nostrip_files = ["usr/libexec/valgrind/*", "usr/lib/valgrind/*"]
hardening = ["!ssp", "!scp", "!pie", "!int"]
# check may be disabled sometimes
options = ["!cross", "!lto"]
exec_wrappers = [("/usr/bin/gsed", "sed")]

match self.profile().arch:
    case "aarch64":
        # builtins for LSE reference getauxval from libc
        # which we aren't linking to, so eliminate them
        tool_flags["CFLAGS"] += ["-mno-outline-atomics"]
        # does not build
        options += ["!check"]
    case "ppc64le" | "ppc64" | "ppc":
        # lld causes the tools to segfault on start
        hostmakedepends += [f"binutils-{self.profile().arch}"]
        tool_flags["LDFLAGS"] += ["-fuse-ld=bfd"]
        # does not build
        options += ["!check"]


@subpackage("valgrind-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel(extra=["usr/share/doc"])

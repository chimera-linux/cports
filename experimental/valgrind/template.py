pkgname = "valgrind"
pkgver = "3.21.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-mpicc"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."  # junk in main dir prevents reliable out of tree build
hostmakedepends = [
    "gmake",
    "gsed",
    "pkgconf",
    "perl",
    "automake",
    "libtool",
]
makedepends = ["libomp-devel", "linux-headers"]
depends = ["perl", "python"]
pkgdesc = "Instrumentation framework for building dynamic analysis tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://valgrind.org"
source = f"https://sourceware.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "10ce1618bb3e33fad16eb79552b0a3e1211762448a0d7fce11c8a6243b9ac971"
debug_level = 1
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE", "-fPIC"], "LDFLAGS": ["-fPIC"]}
nostrip_files = ["usr/libexec/valgrind/*", "usr/lib/valgrind/*"]
hardening = ["!ssp", "!scp", "!pie", "!int"]
options = ["!cross", "!lto"]
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("valgrind-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel(extra=["usr/share/doc"])

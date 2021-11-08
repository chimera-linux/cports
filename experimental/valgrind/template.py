# this is not fully functional right now; it builds and runs, but valgrind
# will not properly track allocations (oddly enough, it will track frees)
pkgname = "valgrind"
pkgver = "3.18.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-mpicc"]
make_cmd = "gmake"
make_dir = "." # junk in main dir prevents reliable out of tree build
hostmakedepends = [
    "gmake", "gsed", "pkgconf", "perl", "binutils", "automake", "libtool"
]
makedepends = ["libomp-devel"]
depends = ["perl"]
pkgdesc = "Instrumentation framework for building dynamic analysis tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://valgrind.org"
source = f"https://sourceware.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "00859aa13a772eddf7822225f4b46ee0d39afbe071d32778da4d99984081f7f5"
tool_flags = {
    "CFLAGS": ["-no-integrated-as"],
    "CXXFLAGS": ["-no-integrated-as"],
    "LDFLAGS": ["-fuse-ld=bfd"],
}
nostrip_files = [
    "usr/libexec/valgrind/*"
]
hardening = ["!ssp", "!pie"]
# uses binutils; makes glibc assumptions in tests
options = ["!cross", "!check", "!scanshlibs", "!scanrundeps"]
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]

def pre_configure(self):
    self.cp(self.files_path / "musl.supp", self.cwd)

    self.do(self.chroot_cwd / "autogen.sh", [])

    with open(self.cwd / "include/a.out.h", "w") as f:
        f.write("#include <linux/a.out.h>\n")

@subpackage("valgrind-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/doc"])

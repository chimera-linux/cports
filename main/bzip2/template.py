pkgname = "bzip2"
# update bzip2.pc if the version changes (and check if upstreamed)
pkgver = "1.0.8"
pkgrel = 3
hostmakedepends = ["pkgconf"]
provides = [self.with_pkgver("libbz2")]
pkgdesc = "Freely available, patent free, high-quality data compressor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:bzip2"
url = "https://sourceware.org/bzip2"
source = f"https://sourceware.org/pub/bzip2/bzip2-{pkgver}.tar.gz"
sha256 = "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["bootstrap"]


def build(self):
    cmd = ["make", f"-j{self.make_jobs}"]
    eargs = [
        "CFLAGS=" + self.get_cflags(shell=True),
        "LDFLAGS=" + self.get_ldflags(shell=True),
    ]
    self.do(*cmd, "-f", "Makefile-libbz2_so", *eargs)
    self.do(*cmd, "bzip2recover", "libbz2.a", *eargs)


def check(self):
    self.do("make", "check")


def install(self):
    self.cp("bzip2-shared", "bzip2")

    self.install_bin("bzip2")
    self.install_bin("bzip2recover")

    self.install_link("usr/bin/bunzip2", "bzip2")
    self.install_link("usr/bin/bzcat", "bzip2")

    self.install_bin("bzmore")

    self.install_lib(f"libbz2.so.{pkgver}")
    self.install_link("usr/lib/libbz2.so", f"libbz2.so.{pkgver}")
    self.install_link("usr/lib/libbz2.so.1", f"libbz2.so.{pkgver}")
    self.install_link("usr/lib/libbz2.so.1.0", f"libbz2.so.{pkgver}")

    self.install_file("libbz2.a", "usr/lib")
    self.install_file("bzlib.h", "usr/include")
    self.install_file(self.files_path / "bzip2.pc", "usr/lib/pkgconfig")

    self.install_man("bzip2.1")
    self.install_link("usr/share/man/man1/bunzip2.1", "bzip2.1")
    self.install_link("usr/share/man/man1/bzcat.1", "bzip2.1")
    self.install_link("usr/share/man/man1/bzip2recover.1", "bzip2.1")

    self.install_license("LICENSE")


@subpackage("bzip2-devel")
def _(self):
    self.provides = [self.with_pkgver("libbz2-devel")]

    return self.default_devel()

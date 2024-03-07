pkgname = "sbcl"
pkgver = "2.4.2"
pkgrel = 0
archs = ["aarch64", "ppc", "ppc64le", "riscv64", "x86_64"]
hostmakedepends = [
    "ecl",
    "ecl-devel",
    "gc-devel",
    "gmake",
    "gmp-devel",
    "libatomic_ops-devel",
    "libffi-devel",
    "linux-headers",
    "texinfo",
]
makedepends = ["zstd-devel"]
checkdepends = ["strace"]
pkgdesc = "Steel Bank Common Lisp"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:sbcl"
url = "https://www.sbcl.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}-source.tar.bz2"
sha256 = "fc03cb52d12aafe8759e6328450a201bbddf89b17071a4e83f39e80b43ddef0f"
options = ["!cross", "!lto"]
# GNUMAKE disregarded in tests
exec_wrappers = [("/usr/bin/gmake", "make")]


def do_configure(self):
    pass


def do_build(self):
    self.do(
        "sh", "make.sh", "ecl", "--prefix=/usr", "--with-sb-core-compression"
    )
    self.do("gmake", "info", wrksrc="doc/manual")


def do_check(self):
    self.do("sh", "run-tests.sh", wrksrc="tests")


def do_install(self):
    self.do(
        "sh",
        "install.sh",
        env={"INSTALL_ROOT": str(self.chroot_destdir / "usr")},
    )

    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/doc/sbcl/COPYING")

pkgname = "txr"
pkgver = "293"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "configure"
configure_args = ["--parallelmake", "--prefix=/usr"]
make_cmd = "gmake"
make_check_target = "tests"
hostmakedepends = ["bash", "gmake"]
makedepends = ["libffi-devel", "zlib-devel"]
pkgdesc = "Data munging language"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:txr"
url = "https://www.nongnu.org/txr"
source = f"https://www.kylheku.com/cgit/{pkgname}/snapshot/{pkgname}-{pkgver}.tar.bz2"
sha256 = "6fc21ae7332f98f97af35ad3ca1808d0043c4c85384c4e7bebcfce967e36fa5c"
hardening = ["vis"]
options = ["!cross", "!lto"]


def init_configure(self):
    self.env["txr_shell"] = "/usr/bin/bash"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("METALICENSE")

    self.rm(self.destdir / "usr/share/txr/LICENSE")
    self.rm(self.destdir / "usr/share/txr/METALICENSE")

    # hardlinks
    for f in ["txrlisp", "txrvm"]:
        self.rm(self.destdir / f"usr/bin/{f}")
        self.install_link("txr", f"usr/bin/{f}")

pkgname = "txr"
pkgver = "298"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "configure"
configure_args = ["--parallelmake", "--prefix=/usr"]
make_check_target = "tests"
hostmakedepends = ["bash"]
makedepends = ["libffi8-devel", "zlib-ng-compat-devel"]
pkgdesc = "Data munging language"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:txr"
url = "https://www.nongnu.org/txr"
source = f"https://www.kylheku.com/cgit/txr/snapshot/txr-{pkgver}.tar.bz2"
sha256 = "49c0f101f3ee549159c3bd90ee0c434ce1c573e4fe23ed764f82e73075a31023"
hardening = ["vis"]
# tests disabled on ppc
options = ["!cross", "!lto"]


def init_configure(self):
    self.env["txr_shell"] = "/usr/bin/bash"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("METALICENSE")

    self.uninstall("usr/share/txr/LICENSE")
    self.uninstall("usr/share/txr/METALICENSE")

    # hardlinks
    for f in ["txrlisp", "txrvm"]:
        self.uninstall(f"usr/bin/{f}")
        self.install_link(f"usr/bin/{f}", "txr")

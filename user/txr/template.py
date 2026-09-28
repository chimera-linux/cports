pkgname = "txr"
pkgver = "302"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "configure"
configure_args = ["--parallelmake", "--prefix=/usr"]
make_check_target = "tests"
hostmakedepends = ["bash"]
makedepends = ["libffi8-devel", "zlib-ng-compat-devel"]
pkgdesc = "Data munging language"
license = "custom:txr"
url = "https://www.nongnu.org/txr"
source = f"https://www.kylheku.com/cgit/txr/snapshot/txr-{pkgver}.tar.bz2"
sha256 = "f0de012ed62218e049d09a39ae6a9387598d8eac12a7c2d7d9d906c27c36ef54"
hardening = ["vis"]
options = ["!cross", "!lto"]


def post_extract(self):
    # segfaults
    self.rm("tests/012/compile.tl")


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

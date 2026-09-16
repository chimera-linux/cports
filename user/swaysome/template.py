pkgname = "swaysome"
pkgver = "2.3.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Workspace namespace navigation"
license = "MIT"
url = "https://gitlab.com/hyask/swaysome"
source = f"{url}/-/archive/{pkgver}/swaysome-{pkgver}.tar.gz"
sha256 = "fb3c23bb1a07e9b4f1c6510287086228f0e0aaee4e63690b0b197725a24a4891"
# no tests defined
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "swaysome"))
    self.install_license("LICENSE")
    self.install_man("swaysome.1")

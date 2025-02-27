pkgname = "swaysome"
pkgver = "2.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Workspace namespace navigation"
license = "MIT"
url = "https://gitlab.com/hyask/swaysome"
source = f"{url}/-/archive/{pkgver}/swaysome-{pkgver}.tar.gz"
sha256 = "162e6118be952fe66eac070e57a25f68f8ffe274cdd6cab7bfe64de36d33b409"
# no tests defined
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/swaysome")
    self.install_license("LICENSE")
    self.install_man("swaysome.1")

pkgname = "sway-overfocus"
pkgver = "0.2.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Better focus navigation for sway and i3"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/korreman/sway-overfocus"
source = f"https://github.com/korreman/sway-overfocus/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4d15bc8a307b58e62e3f1a6bd93820bd18307de4bd921dd646ccc715f2348c71"


def post_install(self):
    self.install_license("LICENSE")

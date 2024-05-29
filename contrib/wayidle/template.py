pkgname = "wayidle"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Wait for wayland compositor idle timeouts"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://git.sr.ht/~whynothugo/wayidle"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f71d7c9f62d39b254b11a716e7ba7da9ae81224bacb8b273ab5d9595b9fa6b7d"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.md")

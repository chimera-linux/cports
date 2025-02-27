pkgname = "wayidle"
pkgver = "1.0.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Wait for wayland compositor idle timeouts"
license = "ISC"
url = "https://git.sr.ht/~whynothugo/wayidle"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "90fd35d0e878a56eb5eef0e16b48599f6e635883cdb4e75f63d85fac305f2f3a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.md")

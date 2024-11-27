pkgname = "wayidle"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Wait for wayland compositor idle timeouts"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://git.sr.ht/~whynothugo/wayidle"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "36f191372658a7ac25a4343bcd227ce06523358ca1801daa807fd07b1cd34d27"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.md")

pkgname = "wayidle"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Wait for wayland compositor idle timeouts"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://git.sr.ht/~whynothugo/wayidle"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e02ee79310c91de44466d245d6a12277d539ff7001fc5e53d3b3edf374512f05"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE.md")

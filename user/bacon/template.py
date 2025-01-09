pkgname = "bacon"
pkgver = "3.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c439767c6ec59ff91fddfdffd7581697c9db051d086c23e928633f73ae0f8533"


def post_install(self):
    self.install_license("LICENSE")

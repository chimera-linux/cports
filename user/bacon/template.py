pkgname = "bacon"
pkgver = "3.9.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cac962e77605079612ac3b4447681b6866113b8dacb56c7014b3b3cea9545f33"


def post_install(self):
    self.install_license("LICENSE")

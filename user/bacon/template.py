pkgname = "bacon"
pkgver = "3.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b5db72bf1be28ac67c2df5ed251fa806091a46af5ebab176a6f30d9566ca25c1"


def post_install(self):
    self.install_license("LICENSE")

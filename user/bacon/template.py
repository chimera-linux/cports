pkgname = "bacon"
pkgver = "3.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a27b37af7e38be0888003eb5da4ce01b803fa78758a1cc8c857a4689e774a0eb"


def post_install(self):
    self.install_license("LICENSE")

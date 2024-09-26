pkgname = "bacon"
pkgver = "2.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff43a713b5a301a90ac4e1432cc119f9e52b2563d71dbafa30546cef4a7aeacd"


def post_install(self):
    self.install_license("LICENSE")

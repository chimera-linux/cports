pkgname = "bacon"
pkgver = "3.16.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cf7f3471883260f7cd56d1b2bcce713463082e64a830bb46489d7e94303b3ba0"


def post_install(self):
    self.install_license("LICENSE")

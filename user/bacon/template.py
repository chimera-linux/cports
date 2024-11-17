pkgname = "bacon"
pkgver = "3.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "640a6a76213ef4b7337c7a3495afba3056ee5d58b3b7aefebe35edfc9c179e16"


def post_install(self):
    self.install_license("LICENSE")

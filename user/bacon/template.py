pkgname = "bacon"
pkgver = "3.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a5819aa6b5a56d089dba3e51ce469845af84b7c6feeba02f21f038ea92accad9"


def post_install(self):
    self.install_license("LICENSE")

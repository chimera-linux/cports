pkgname = "bacon"
pkgver = "3.15.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b162a0e9f827d849c962a5a0623ba9435182e3bf6c8e3fe4630a2446a8326bc7"


def post_install(self):
    self.install_license("LICENSE")

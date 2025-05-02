pkgname = "yggdrasil-keygen"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Yggdrasil key generator brute forcing stronger addresses"
license = "AGPL-3.0-only"
url = "https://github.com/jcgruenhage/yggdrasil-keygen"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8a1918d4bf92c3f729b05344e50d9a1e1d50c1429b4a164588f03a83246d3f4"


def post_install(self):
    self.install_license("LICENSE.md")

pkgname = "rbw"
pkgver = "1.13.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "afe8887b64c4da6e5f33535d02ad4e1fe75c536a55d63291622b4b339522d138"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "rbw"
pkgver = "1.13.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2e3181417732b5ab32456a1babff2febeee695604e85db2c94668270ed8a2036"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "iwmenu"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["iwd"]
pkgdesc = "Menu-driven Wi-Fi management interface"
license = "GPL-3.0-or-later"
url = "https://github.com/e-tho/iwmenu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9537bf39032a229558e34f7e98700bb0f1924d818aa4bc55ee92c7ddf4bd73b9"
# no tests defined
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "atomic64 shenanigans"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/iwmenu")

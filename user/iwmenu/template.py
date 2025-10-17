pkgname = "iwmenu"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["iwd"]
pkgdesc = "Menu-driven Wi-Fi management interface"
license = "GPL-3.0-or-later"
url = "https://github.com/e-tho/iwmenu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bc178eb9bdb63b4221a539fc8a2b3710528623f3b4ba87c54b21f0bf6132ba0e"
# no tests defined
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "atomic64 shenanigans"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/iwmenu")

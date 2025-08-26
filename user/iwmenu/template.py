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
sha256 = "7be3ce6c2cddd3bc5fef7a0ca935fba0490b8e621e2e8188b4e88a85af1c8351"
# no tests defined
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "atomic64 shenanigans"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/iwmenu")

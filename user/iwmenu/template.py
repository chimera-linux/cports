pkgname = "iwmenu"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["iwd"]
pkgdesc = "Menu-driven Wi-Fi management interface"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/e-tho/iwmenu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ddc14257f74c0d8d42ccc066a30317770d979158013450d4515338a0cf8001da"
# no tests defined
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/iwmenu")

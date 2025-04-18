pkgname = "binwalk"
pkgver = "3.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "fontconfig-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
# two tests depend on /usr/share/man/man2/accept.2.gz
checkdepends = ["man-pages-devel"]
pkgdesc = "Firmware analysis tool"
license = "MIT"
url = "https://github.com/ReFirmLabs/binwalk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "06f595719417b70a592580258ed980237892eadc198e02363201abe6ca59e49a"

if self.profile().wordsize != 64:
    broken = "explicitly asserts 64-bit"


def post_install(self):
    self.install_license("LICENSE")

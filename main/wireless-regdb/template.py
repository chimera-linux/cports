pkgname = "wireless-regdb"
pkgver = "2024.10.07"
pkgrel = 0
build_style = "makefile"
make_install_args = ["FIRMWARE_PATH=/usr/lib/firmware"]
pkgdesc = "Wireless CRDA database"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb"
source = f"https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-{pkgver}.tar.xz"
sha256 = "f76f2bd79a653e9f9dd50548d99d03a4a4eb157da056dfd5892f403ec28fb3d5"
# just files
options = ["!check"]


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")

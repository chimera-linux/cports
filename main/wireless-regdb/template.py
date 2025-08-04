pkgname = "wireless-regdb"
pkgver = "2025.07.10"
pkgrel = 0
build_style = "makefile"
make_install_args = ["FIRMWARE_PATH=/usr/lib/firmware"]
pkgdesc = "Wireless CRDA database"
license = "ISC"
url = "https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb"
source = f"https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-{pkgver}.tar.xz"
sha256 = "a8340bcdcd1b5db6c79149879d122b170f3bb075381718d4f429ad831a6fa28d"
# just files
options = ["!check"]


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")

pkgname = "wireless-regdb"
pkgver = "2025.02.20"
pkgrel = 0
build_style = "makefile"
make_install_args = ["FIRMWARE_PATH=/usr/lib/firmware"]
pkgdesc = "Wireless CRDA database"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb"
source = f"https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-{pkgver}.tar.xz"
sha256 = "57f8e7721cf5a880c13ae0c202edbb21092a060d45f9e9c59bcd2a8272bfa456"
# just files
options = ["!check"]


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")

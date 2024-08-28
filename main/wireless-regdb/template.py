pkgname = "wireless-regdb"
pkgver = "2024.07.04"
pkgrel = 0
build_style = "makefile"
make_install_args = ["FIRMWARE_PATH=/usr/lib/firmware"]
pkgdesc = "Wireless CRDA database"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb"
source = f"https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-{pkgver}.tar.xz"
sha256 = "9832a14e1be24abff7be30dee3c9a1afb5fdfcf475a0d91aafef039f8d85f5eb"
# just files
options = ["!check"]


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")

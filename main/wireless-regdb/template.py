pkgname = "wireless-regdb"
pkgver = "2026.09.03"
pkgrel = 0
build_style = "makefile"
make_install_args = ["FIRMWARE_PATH=/usr/lib/firmware"]
pkgdesc = "Wireless CRDA database"
license = "ISC"
url = "https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb"
source = f"https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-{pkgver}.tar.xz"
sha256 = "b22e0901227b820cd1c280abe681a15b773a5103a5e10dc442e94ebb34cbf58d"
# just files
options = ["!check"]


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")

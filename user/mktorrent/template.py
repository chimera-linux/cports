pkgname = "mktorrent"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Command line utility to create BitTorrent metainfo files"
license = "GPL-2.0-or-later"
url = "https://github.com/pobrn/mktorrent"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d0f47500192605d01b5a2569c605e51ed319f557d24cfcbcb23a26d51d6138c9"
# No tests included
options = ["!check"]

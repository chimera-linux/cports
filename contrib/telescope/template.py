pkgname = "telescope"
pkgver = "0.9.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "libgrapheme-devel",
    "libretls-devel",
    "openssl-devel",
    "ncurses-devel",
]
pkgdesc = "Terminal browser for gemini/gopher/finger"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC AND Unicode-3.0 AND BSD-3-Clause AND MIT"
url = "https://telescope.omarpolo.com"
source = f"https://ftp.omarpolo.com/telescope-{pkgver}.tar.gz"
sha256 = "fed1ef4db27e713c8719f1e32cc30c911532e90d1bd8aa507acf3db74973c7ac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

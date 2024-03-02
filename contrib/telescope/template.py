pkgname = "telescope"
pkgver = "0.9"
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
sha256 = "c963c82afde87ed5397ddd6a399ff7dfdbd32144ce742cb5a11c2ad6476d7cf5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

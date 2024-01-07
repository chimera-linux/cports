pkgname = "epson-inkjet-printer-escpr"
pkgver = "1.8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-cupsppddir=/usr/share/ppd",
    "--with-cupsfilterdir=/usr/lib/cups/filter",
]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake"]
makedepends = ["cups-devel"]
depends = ["cups-filters"]
pkgdesc = "Epson Inkjet Printer Driver (ESC/P-R)"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://download.ebz.epson.net/dsc/search/01/search?OSC=LX&productName=B700"
source = f"https://download3.ebz.epson.net/dsc/f/03/00/15/48/01/7599a456504eeb6f7052b6f955735fc94475eca9/epson-inkjet-printer-escpr-{pkgver}-1.tar.gz"
sha256 = "d0cf07fb2404b97d49fa1df62531eec0d9d985c84746e62556dc3cacd0ab0386"

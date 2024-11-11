pkgname = "epson-inkjet-printer-escpr"
pkgver = "1.8.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-cupsppddir=/usr/share/ppd",
    "--with-cupsfilterdir=/usr/lib/cups/filter",
]
make_dir = "."
hostmakedepends = ["automake", "slibtool"]
makedepends = ["cups-devel"]
depends = ["cups-filters"]
pkgdesc = "Epson Inkjet Printer Driver"
subdesc = "ESC/P-R"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://download.ebz.epson.net/dsc/search/01/search?OSC=LX&productName=B700"
source = f"https://download3.ebz.epson.net/dsc/f/03/00/16/21/81/74d098a47c3a616713079c9cd5904b468bb33dea/epson-inkjet-printer-escpr-{pkgver}-1.tar.gz"
sha256 = "8556d7e0e5cf7b8cb7ed2ce3bb7b957579557635f80c548dfc0d849b3dde09c4"

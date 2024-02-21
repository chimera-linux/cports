pkgname = "epson-inkjet-printer-escpr"
pkgver = "1.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-cupsppddir=/usr/share/ppd",
    "--with-cupsfilterdir=/usr/lib/cups/filter",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["automake", "gmake", "libtool"]
makedepends = ["cups-devel"]
depends = ["cups-filters"]
pkgdesc = "Epson Inkjet Printer Driver (ESC/P-R)"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://download.ebz.epson.net/dsc/search/01/search?OSC=LX&productName=B700"
source = f"https://download3.ebz.epson.net/dsc/f/03/00/15/57/25/a928e7d08c825ef1cdb892e70318d986720cef8a/epson-inkjet-printer-escpr-{pkgver}-1.tar.gz"
sha256 = "3cf19fc139886997146c0b31d86fcbc718e11b76d1b9b5aaf391f13405c9450e"

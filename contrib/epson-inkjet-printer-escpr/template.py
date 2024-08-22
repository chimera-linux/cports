pkgname = "epson-inkjet-printer-escpr"
pkgver = "1.8.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-cupsppddir=/usr/share/ppd",
    "--with-cupsfilterdir=/usr/lib/cups/filter",
]
make_dir = "."
hostmakedepends = ["automake", "libtool"]
makedepends = ["cups-devel"]
depends = ["cups-filters"]
pkgdesc = "Epson Inkjet Printer Driver"
subdesc = "ESC/P-R"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://download.ebz.epson.net/dsc/search/01/search?OSC=LX&productName=B700"
source = f"https://download3.ebz.epson.net/dsc/f/03/00/15/68/89/fbff579f15226ffcc4a16895bd6bce6842277802/epson-inkjet-printer-escpr-{pkgver}-1.tar.gz"
sha256 = "27ca5426abece5ff1da859caa5ac4bc993b0a00e8ea74af63ffd9960c6a36a24"

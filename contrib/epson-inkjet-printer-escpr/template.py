pkgname = "epson-inkjet-printer-escpr"
pkgver = "1.8.2"
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
source = f"https://download3.ebz.epson.net/dsc/f/03/00/15/37/36/9209d0195bbe0743c8f9f427bdc5d09186d72ba2/epson-inkjet-printer-escpr-{pkgver}-1.tar.gz"
sha256 = "14d5cdf300b5ff930ef268a2805568f4abf9e9cc9df17be2d76e77e3afdc5e42"

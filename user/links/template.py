pkgname = "links"
pkgver = "2.30"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr", "--mandir=PREFIX/share/man"]
hostmakedepends = [
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Lynx-like text WWW browser"
license = "GPL-2.0-or-later"
url = "http://links.twibright.com"
source = f"{url}/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "7f0d54f4f7d1f094c25c9cbd657f98bc998311122563b1d757c9aeb1d3423b9e"

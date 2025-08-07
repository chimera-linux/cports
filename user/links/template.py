pkgname = "links"
pkgver = "2.30"
pkgrel = 1
build_style = "gnu_configure"
# TODO: configure fails with 'conditional "am__fastdepCXX" was never defined.'???
configure_gen = []
make_install_args = ["install", "mandir=/usr/share/man"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Lynx-like text WWW browser"
license = "GPL-2.0-or-later"
url = "http://links.twibright.com"
source = f"{url}/download/links-{pkgver}.tar.gz"
sha256 = "7f0d54f4f7d1f094c25c9cbd657f98bc998311122563b1d757c9aeb1d3423b9e"
hardening = ["vis", "cfi"]

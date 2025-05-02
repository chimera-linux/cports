pkgname = "pcsc-tools"
pkgver = "1.7.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "pkgconf",
]
makedepends = ["pcsc-lite-devel"]
depends = [
    "pcsc-perl",
    # TODO: perl-gtk3
    "perl-glib",
    "perl-libintl-perl",
]
pkgdesc = "Tools for PCSC"
license = "GPL-2.0-or-later"
url = "https://pcsc-tools.apdu.fr"
source = f"{url}/pcsc-tools-{pkgver}.tar.bz2"
sha256 = "c3b6d2b7a40bc066ebb8cd2512fb42e2b787a5c491a5715b8741743f4edb8cc2"

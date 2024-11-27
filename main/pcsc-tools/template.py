pkgname = "pcsc-tools"
pkgver = "1.7.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pcsc-tools.apdu.fr"
source = f"{url}/pcsc-tools-{pkgver}.tar.bz2"
sha256 = "fd6fcc25e8140f613b3bf44b02eda4a8a429ee4939fb777f474e2c829f7b472c"

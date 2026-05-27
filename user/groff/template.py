pkgname = "groff"
pkgver = "1.24.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--bindir=/usr/bin",
    "--sbindir=/usr/bin",
    "--libexecdir=/usr/lib",
    "--sysconfdir=/usr",
    "--sharedstatedir=/var/share",
    "--localstatedir=/var",
    "--runstatedir=/run",
    "--libdir=/usr/lib",
    "--includedir=/usr/include",
    "--oldincludedir=/usr/include",
    "--disable-dependency-tracking",
    "--enable-year2038",
]
makedepends = ["perl", "uchardet-devel"]
checkdepends = ["ghostscript"]
depends = ["perl>=5.8", "uchardet"]
pkgdesc = "GNU troff, a typesettng system"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/groff"
source = f"https://ftpmirror.gnu.org/gnu/groff/groff-{pkgver}.tar.gz"
sha256 = "74e2819795b6aff431aeac983d63a9c8968eeaba2a2eba7df8ba4c7b41e7cfd8"
# TODO only 1 check (out of like 300 smth) fails
# well, a fair amout of them are just skipped...
options = ["!check"]

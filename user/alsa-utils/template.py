pkgname = "alsa-utils"
pkgver = "1.2.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-udev-rules-dir=no"]
make_dir = "."
hostmakedepends = [
    "alsa-lib-devel",
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = ["alsa-lib-devel", "linux-headers", "ncurses-devel"]
pkgdesc = "ALSA utilities"
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/utils/alsa-utils-{pkgver}.tar.bz2"
sha256 = "0794c74d33fed943e7c50609c13089e409312b6c403d6ae8984fc429c0960741"

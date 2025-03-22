pkgname = "alsa-utils"
pkgver = "1.2.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-udev-rules-dir=no"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-devel"]
makedepends = ["alsa-lib-devel", "linux-headers", "ncurses-devel"]
depends = ["alsa-lib", "ncurses"]
pkgdesc = "Advanced Linux Sound Architecture library - Utilities"
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/utils/alsa-utils-{pkgver}.tar.bz2"
sha256 = "1702a6b1cdf9ba3e996ecbc1ddcf9171e6808f5961d503d0f27e80ee162f1daa"

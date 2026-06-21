pkgname = "alsa-utils"
pkgver = "1.2.16"
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
sha256 = "092399d5e8749a1d5e188e393157521cec4b75693b60ebb79bbce728cff2232c"

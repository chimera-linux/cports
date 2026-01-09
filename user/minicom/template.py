pkgname = "minicom"
pkgver = "2.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Serial communication program"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/minicom-team/minicom"
source = f"{url}/-/archive/{pkgver}/minicom-{pkgver}.tar.gz"
sha256 = "66ff82661c3cc49ab2e447f8a070ec1a64ba71d64219906d80a49da284a5d43e"

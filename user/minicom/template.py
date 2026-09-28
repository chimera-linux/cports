pkgname = "minicom"
pkgver = "2.11.1"
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
sha256 = "b296b0e5795ca143fb1ffa78f46fd294daddfccd720faf9909a842d2f70c564e"

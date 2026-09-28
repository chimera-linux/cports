pkgname = "libkcddb"
pkgver = "26.08.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
# need net
make_check_args = ["-E", "(.*lookuptest|.*submittest|.*musicbrainz.*|utf8test)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "libmusicbrainz-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE library for retrieving audio metadata"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/multimedia/libkcddb"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkcddb-{pkgver}.tar.xz"
sha256 = "2d86bd59ff8d1d5474e594ca0a8ce2ef5a1cabf9a27f357c6e83c9920dd1dafb"


@subpackage("libkcddb-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()

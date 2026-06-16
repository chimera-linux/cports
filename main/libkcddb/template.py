pkgname = "libkcddb"
pkgver = "26.04.2"
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
url = "https://api.kde.org/libkcddb/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkcddb-{pkgver}.tar.xz"
sha256 = "d3b8d83bf5482cc5ed2d5830960940fb0397fe7fcfbbacf85c8c2b68f752a38b"


@subpackage("libkcddb-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()

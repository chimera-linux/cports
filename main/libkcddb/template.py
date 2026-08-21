pkgname = "libkcddb"
pkgver = "26.08.0"
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
sha256 = "ca7e25cffb5d37e4a1e256d85bb954577bd1ef6440711b0ffd0fc760d64842ba"


@subpackage("libkcddb-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()

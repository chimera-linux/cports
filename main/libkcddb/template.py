pkgname = "libkcddb"
pkgver = "25.04.1"
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
sha256 = "af48bad3f94614fec1f1e3793a2f8808effaebbfbe1603c2d6f2748daff84bec"


@subpackage("libkcddb-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()

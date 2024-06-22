pkgname = "libkcddb"
pkgver = "24.05.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://api.kde.org/libkcddb/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkcddb-{pkgver}.tar.xz"
sha256 = "71b72b19b70f428980c7e3487a9e94e67d4537eba56834e9a2c0a0f07b4e2aff"


@subpackage("libkcddb-devel")
def _devel(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()

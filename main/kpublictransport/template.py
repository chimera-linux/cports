pkgname = "kpublictransport"
pkgver = "26.04.2"
pkgrel = 0
build_style = "cmake"
# at least updatetest & cachetest flaky when parallel
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kirigami-addons-devel",
    "networkmanager-qt-devel",
    "protobuf-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtlocation-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE library for accessing public transport information"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kpublictransport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpublictransport-{pkgver}.tar.xz"
)
sha256 = "9669fdc271067f82851cf7804fc62fc0a5b228d488f9e9217a3b65d0e839c6b2"


@subpackage("kpublictransport-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel", "zlib-ng-compat-devel"]
    return self.default_devel()

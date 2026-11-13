pkgname = "kpublictransport"
pkgver = "26.08.3"
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
url = "https://community.kde.org/KDE_PIM"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpublictransport-{pkgver}.tar.xz"
)
sha256 = "603ad9793eb63151ac08d0d32fc1a18bc9cb4a3d5c6d05e41fcf7dd073de47a7"


@subpackage("kpublictransport-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel", "zlib-ng-compat-devel"]
    return self.default_devel()

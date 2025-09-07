pkgname = "kitinerary"
pkgver = "25.08.0"
pkgrel = 1
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# extractortest: difference in AT/österreich key
# knowledgedbtest: flaky SIBBUS crash in ki18n IsoCodesCache::subdivisionCount from accessing cache (weird pointer stuff)
# airportdbtest: the same
make_check_args = ["-E", "(extractortest|knowledgedbtest|airportdbtest)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcalendarcore-devel",
    "kcontacts-devel",
    "ki18n-devel",
    "kmime-devel",
    "kpkpass-devel",
    "libphonenumber-devel",
    "libxml2-devel",
    "openssl3-devel",
    "poppler-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
    "zlib-ng-compat-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE travel reservation parsing library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kitinerary/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kitinerary-{pkgver}.tar.xz"
sha256 = "635530c31d67fc35f5f5bcdf43f06d896e47b423d02df6546ef3c5fea1d212c6"


@subpackage("kitinerary-devel")
def _(self):
    self.depends += [
        "kcalendarcore-devel",
        "kcontacts-devel",
        "kmime-devel",
        "kpkpass-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

pkgname = "kitinerary"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
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
sha256 = "da895934f27f99ba7b463a4df8f365fb4b12f15458c266e910c13ebb8ef00784"


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

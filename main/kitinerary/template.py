pkgname = "kitinerary"
pkgver = "24.12.0"
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
    "openssl-devel",
    "poppler-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
    "zlib-ng-compat-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE travel reservation parsing library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kitinerary/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kitinerary-{pkgver}.tar.xz"
sha256 = "4c11339a5bce980bd061a4437a943200fae82e104bd8472f3b2f7dc36f82b5c7"


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

pkgname = "kitinerary"
pkgver = "24.08.1"
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
sha256 = "69e31024bef80836e1cf5eaf1543fe9a0ca07d7243d4349f9da0a827a1233933"


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

pkgname = "kitinerary"
pkgver = "24.05.1"
pkgrel = 1
build_style = "cmake"
# difference in AT/österreich key
make_check_args = ["-E", "extractortest"]
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
    "libpoppler-devel",
    "libxml2-devel",
    "openssl-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
    "zlib-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE travel reservation parsing library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kitinerary/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kitinerary-{pkgver}.tar.xz"
sha256 = "e1c77f0a8e826fd95f001a6d8fc941906d3e0aad98c2876c77c5e3ba7462d0e6"


@subpackage("kitinerary-devel")
def _devel(self):
    self.depends += [
        "kcalendarcore-devel",
        "kcontacts-devel",
        "kmime-devel",
        "kpkpass-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

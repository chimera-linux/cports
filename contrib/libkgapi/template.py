pkgname = "libkgapi"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
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
    "kwallet-devel",
    "libsasl-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE library for accessing Google services"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/libkgapi/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkgapi-{pkgver}.tar.xz"
sha256 = "d878b8521aa83276f8807f97cfa5b307988a6094cec0556147faca5ae9173981"
# tests all segfault with missing data
options = ["!check"]


@subpackage("libkgapi-devel")
def _devel(self):
    self.depends += [
        "kcontacts-devel",
        "kcalendarcore-devel",
    ]
    return self.default_devel()

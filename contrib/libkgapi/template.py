pkgname = "libkgapi"
pkgver = "24.08.0"
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
sha256 = "1db9e5e2b1bb550b36780f9ab5e571e15b75d397c5555e0e18fd8e3541ddc915"
# tests all segfault with missing data
options = ["!check"]


@subpackage("libkgapi-devel")
def _(self):
    self.depends += [
        "kcontacts-devel",
        "kcalendarcore-devel",
    ]
    return self.default_devel()

pkgname = "libkgapi"
pkgver = "25.08.3"
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
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/libkgapi/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkgapi-{pkgver}.tar.xz"
sha256 = "5a6590da04cf4a0c3b53f2a0c7d7c97cdf57f63854a0a4978c0859243bfbd15e"
# tests all segfault with missing data
options = ["!check"]


@subpackage("libkgapi-devel")
def _(self):
    self.depends += [
        "kcontacts-devel",
        "kcalendarcore-devel",
    ]
    return self.default_devel()

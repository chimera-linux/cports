pkgname = "libkgapi"
pkgver = "24.05.2"
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
sha256 = "c317c96c996708ff86bb2e0de0ddcdb54285948b136e3073969c60c9f85f1948"
# tests all segfault with missing data
options = ["!check"]


@subpackage("libkgapi-devel")
def _devel(self):
    self.depends += [
        "kcontacts-devel",
        "kcalendarcore-devel",
    ]
    return self.default_devel()

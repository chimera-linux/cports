pkgname = "kmime"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
# fails on ppc64le with wrong encoding
make_check_args = ["-E", "(headertest|messagetest)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "qt6-qttools-devel",
]
makedepends = [
    "kcodecs-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE library for mail messages"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmime/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmime-{pkgver}.tar.xz"
sha256 = "9e5aa90d8a2314b5fbc015f066922f2e1fa529daad3b76dfd351567a954353c2"


@subpackage("kmime-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

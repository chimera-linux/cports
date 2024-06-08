pkgname = "kmime"
pkgver = "24.05.0"
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
sha256 = "7c044974ac1f3acde01804766b24ebe17b7413201e78ea4ff9f4f0d77e3bb8b9"


@subpackage("kmime-devel")
def _devel(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

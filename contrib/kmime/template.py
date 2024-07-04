pkgname = "kmime"
pkgver = "24.05.2"
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
sha256 = "d82f38dcf97c6491c6b7367db8b18a65acb594d7eb752543dc23c65d4abab6a5"


@subpackage("kmime-devel")
def _devel(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()

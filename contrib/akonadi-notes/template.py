pkgname = "akonadi-notes"
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
    "ki18n-devel",
    "kmime-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Akonadi notes libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/akonadi-notes/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-notes-{pkgver}.tar.xz"
)
sha256 = "aaf37d4a840a4a3a25e955eb7b60e650d2b7f2ab30bf77c48774744de5b26131"


@subpackage("akonadi-notes-devel")
def _devel(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()

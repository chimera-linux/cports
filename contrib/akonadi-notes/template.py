pkgname = "akonadi-notes"
pkgver = "24.05.1"
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
sha256 = "a8e01508fd1ecc88cffdb37fdd3f0d3fca90e8b31c18703aaad774a3e2ae4f1f"


@subpackage("akonadi-notes-devel")
def _devel(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()

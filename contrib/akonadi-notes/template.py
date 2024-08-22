pkgname = "akonadi-notes"
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
sha256 = "13279448fb1186a3553f7012909b943f4cf476ca5b11e4edc7e70bdf6940b78d"


@subpackage("akonadi-notes-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()

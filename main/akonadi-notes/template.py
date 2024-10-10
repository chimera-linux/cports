pkgname = "akonadi-notes"
pkgver = "24.08.2"
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
sha256 = "2dc30e224bea0f3b585cb71d6cc099741de9bedb8e6e3f06d7a9cefa349e0fde"


@subpackage("akonadi-notes-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()

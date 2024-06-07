pkgname = "akonadi-notes"
pkgver = "24.05.0"
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
sha256 = "9976f66e60c0bca25a7b33eec8711f43c14a97db1e659cdea914968ed2431990"


@subpackage("akonadi-notes-devel")
def _devel(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()

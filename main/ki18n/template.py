pkgname = "ki18n"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
# similar tests broken as alpine
make_check_args = ["-E", "(kcatalog|kcountry|klocalizedstring)test"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
depends = ["iso-codes"]
checkdepends = [
    "iso-codes-locale",
    *depends,
]
pkgdesc = "KDE Gettext-based UI text internationalization"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://api.kde.org/frameworks/ki18n/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
sha256 = "736ae10e3a8c5dced155d3347f9dbd91c34f485d7495815f85f4d624681a1860"
hardening = ["vis"]


@subpackage("ki18n-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

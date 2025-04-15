pkgname = "ki18n"
pkgver = "6.13.0"
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
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://api.kde.org/frameworks/ki18n/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
sha256 = "008c0a32235dc2a7d3aa2fa9a98a540f1b4baf6ab5efd14839a11fda6e746a14"
hardening = ["vis"]


@subpackage("ki18n-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

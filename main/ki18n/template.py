pkgname = "ki18n"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
# similar tests broken as alpine
make_check_args = ["-E", "(kcatalog|kcountry|klocalizedstring)test"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
depends = ["iso-codes"]
checkdepends = ["iso-codes-locale", *depends]
pkgdesc = "KDE Gettext-based UI text internationalization"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
sha256 = "9fa271c7a33b856451de1ed3ff105626c2763fbd3b11d3210b02cb30de43f2ba"
hardening = ["vis"]


@subpackage("ki18n-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

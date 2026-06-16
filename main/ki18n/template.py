pkgname = "ki18n"
pkgver = "6.27.0"
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
url = "https://api.kde.org/frameworks/ki18n/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
sha256 = "cd812ae95b0e95b40e46a50b9dea6d188eec001be96b1e1a5d962730e5f9bc58"
hardening = ["vis"]


@subpackage("ki18n-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

pkgname = "ki18n"
pkgver = "6.3.0"
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
] + depends
pkgdesc = "KDE Gettext-based UI text internationalization"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://api.kde.org/frameworks/ki18n/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
)
sha256 = "4d95341eba2070fec3901396eb0a68f4a8423337de5ea23fb86b0ea70c957282"
# FIXME: cfi breaks at least ki18n-ktranscripttest
hardening = ["vis", "!cfi"]


@subpackage("ki18n-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()

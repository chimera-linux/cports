pkgname = "ki18n"
pkgver = "6.2.0"
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
checkdepends = [
    "iso-codes-locale",
]
# depends = list(checkdepends)
pkgdesc = "KDE Gettext-based UI text internationalization"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://api.kde.org/frameworks/ki18n/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
)
sha256 = "8aa8f4740db080f4f0c2ce88d0f289740d55caa06b7f76bf2163d0fb9fd3660f"
# FIXME: cfi breaks at least ki18n-ktranscripttest
hardening = ["vis", "!cfi"]


@subpackage("ki18n-devel")
def _devel(self):
    # TODO: self.depends += ["gettext"]? only relevant on host tho

    return self.default_devel()

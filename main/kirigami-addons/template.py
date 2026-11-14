pkgname = "kirigami-addons"
pkgver = "1.16.1"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["qt6-qtmultimedia", "sound-theme-freedesktop"]
depends = ["kirigami", "qt6-qtmultimedia", "sonnet"]
pkgdesc = "Add-ons for the Kirigami framework"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kirigami-addons"
source = f"$(KDE_SITE)/kirigami-addons/kirigami-addons-{pkgver}.tar.xz"
sha256 = "124b01267acf603c3afd9fb9599a33fee7a28d65756890163e9593a3932084dd"
hardening = ["vis"]


@subpackage("kirigami-addons-devel")
def _(self):
    return self.default_devel()

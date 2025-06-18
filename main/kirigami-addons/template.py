pkgname = "kirigami-addons"
pkgver = "1.8.1"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(sounds"  # test_click() Compared values are not the same (0 vs 1), tst_sounds.qml:29
    "|album_qmllistmodel"  # test_saveItem() & test_userCaption() Compared values are not the same (0 vs 1, true vs false), BaseAlbumMaximizeComponentTestCase.qml:(159,178)
    "|album_abstractlistmodel"  # ^ same as above
    "|album_qmlqobjectmodel)",  # ^ same as above
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["qt6-qtmultimedia", "sound-theme-freedesktop"]
depends = ["kirigami", "qt6-qtmultimedia", "sonnet"]
pkgdesc = "Add-ons for the Kirigami framework"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kirigami-addons/html"
source = f"$(KDE_SITE)/kirigami-addons/kirigami-addons-{pkgver}.tar.xz"
sha256 = "00028ae4df99e250518345ea28d9cdf49d700e9acac482734bb51384da11f945"
hardening = ["vis"]


@subpackage("kirigami-addons-devel")
def _(self):
    return self.default_devel()

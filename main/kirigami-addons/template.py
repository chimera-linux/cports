pkgname = "kirigami-addons"
pkgver = "1.12.1"
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
url = "https://api.kde.org/kirigami-addons/html/index.html"
source = f"$(KDE_SITE)/kirigami-addons/kirigami-addons-{pkgver}.tar.xz"
sha256 = "c543a493ce5875f405fb1c9ff6d531060ed082cc6d710e56d46ac42d164207bb"
hardening = ["vis"]


@subpackage("kirigami-addons-devel")
def _(self):
    return self.default_devel()

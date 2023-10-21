pkgname = "kxmlgui"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemviews-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "breeze-icons",
    "dbus",
]
pkgdesc = "KDE Framework for managing menu and toolbar actions"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kxmlgui/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kxmlgui-{pkgver}.tar.xz"
sha256 = "ff22a79fca2737e33c5463d87fad2b46920c8d48c6583268a9ae27097a8ac902"
hardening = ["vis", "cfi"]


@subpackage("kxmlgui-devel")
def _devel(self):
    self.depends += ["kconfig-devel", "kconfigwidgets-devel"]

    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])

pkgname = "kxmlgui"
pkgver = "6.4.0"
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
sha256 = "04952bc7f9eaefc7a55c762d77e65888a2a71e638d3fc7126576dfe645564b0b"
hardening = ["vis"]


@subpackage("kxmlgui-devel")
def _devel(self):
    self.depends += ["kconfig-devel", "kconfigwidgets-devel"]

    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])

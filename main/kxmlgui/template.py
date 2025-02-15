pkgname = "kxmlgui"
pkgver = "6.11.0"
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
    "qt6-qtbase-private-devel",  # qlocale_p.h
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kxmlgui-{pkgver}.tar.xz"
sha256 = "69c3a6a6363bdbe3ccbace76e23c6ccec173eb0f9c1954ef7317d998d6edb6fc"
hardening = ["vis"]


@subpackage("kxmlgui-devel")
def _(self):
    self.depends += ["kconfig-devel", "kconfigwidgets-devel"]

    return self.default_devel()

pkgname = "systemsettings"
pkgver = "6.7.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "kitemviews-devel",
    "kpackage-devel",
    "krunner-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "plasma-workspace-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["plasma-workspace"]
pkgdesc = "KDE System settings"
license = "GPL-2.0-or-later"
url = "https://userbase.kde.org/System_Settings"
source = f"$(KDE_SITE)/plasma/{pkgver}/systemsettings-{pkgver}.tar.xz"
sha256 = "317a21165709d61796fba19f5454397577ffd8aa96655b29dd286a1df252cddb"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x100000"]}
hardening = ["vis"]

pkgname = "systemsettings"
pkgver = "6.3.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://userbase.kde.org/System_Settings"
source = f"$(KDE_SITE)/plasma/{pkgver}/systemsettings-{pkgver}.tar.xz"
sha256 = "0d0325a27b8833925b486c7c0ed7ca56f71f94d1fca2ee8afd8c87ec126f6b6f"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x100000"]}
hardening = ["vis"]

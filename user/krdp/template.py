pkgname = "krdp"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "freerdp",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "freerdp-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kpipewire-devel",
    "kstatusnotifieritem-devel",
    "libxkbcommon-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "qtkeychain-devel",
    "wayland-devel",
]
depends = ["freerdp"]
pkgdesc = "KDE RDP server library and examples"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/krdp"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/krdp-{pkgver}.tar.xz"
sha256 = "efc167a1b78d216a28a62fd3cc99818502862ba841eff17593ee15721ce145d5"
# noise
tool_flags = {
    "CXXFLAGS": [
        "-Wno-deprecated-declarations",
    ]
}


def post_install(self):
    self.uninstall("usr/lib/systemd/user")

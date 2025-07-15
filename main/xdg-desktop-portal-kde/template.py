pkgname = "xdg-desktop-portal-kde"
pkgver = "6.4.3"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
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
    "kcrash-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kwayland-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qxkbcommon_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
depends = [
    "kiconthemes",
    "kio-fuse",
    "plasma-workspace",
    "xdg-desktop-portal",
]
checkdepends = [
    "dbus",
    "python-gobject",
    *depends,
]
pkgdesc = "Backend implementation for xdg-desktop-portal using Qt/KF6"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/xdg-desktop-portal-kde"
source = f"$(KDE_SITE)/plasma/{pkgver}/xdg-desktop-portal-kde-{pkgver}.tar.xz"
sha256 = "3fec71e005abe83b3d593a74bc3304c178d605883fe3b77f915c64cf45c1fc27"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")

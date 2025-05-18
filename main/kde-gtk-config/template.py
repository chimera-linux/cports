pkgname = "kde-gtk-config"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "sassc",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE settings synchronization for GTK applications"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kde-gtk-config"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-gtk-config-{pkgver}.tar.xz"
sha256 = "ca066da84272280c3fd6a181970d94f39e117bec8cee91d71a2e252c2145efcf"

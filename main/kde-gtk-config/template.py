pkgname = "kde-gtk-config"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
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
sha256 = "4ef9e07cc262262cf4fd1fd3e43494be20a2487c6b487584f0dea6bc565f98f9"

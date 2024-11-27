pkgname = "kde-gtk-config"
pkgver = "6.2.4"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kde-gtk-config"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-gtk-config-{pkgver}.tar.xz"
sha256 = "e801a162e859766182bccfd2d4abd7093dbbde95183e276ad4de8192151e5645"

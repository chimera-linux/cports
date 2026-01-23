pkgname = "flatpak-kcm"
pkgver = "6.5.5"
pkgrel = 0
build_style = "cmake"
# segfaults in libflatpak probably due to checking system-repo related stuff
# in chroot
make_check_args = ["-E", "flatpakpermissiontest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "flatpak-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "kservice-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE Flatpak permissions KCM"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/flatpak-kcm"
source = f"$(KDE_SITE)/plasma/{pkgver}/flatpak-kcm-{pkgver}.tar.xz"
sha256 = "f22c83bf44aed68238d59bd2965d417f4be72db5b96a9b25c2f6049d9951d206"
hardening = ["vis"]

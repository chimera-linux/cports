pkgname = "flatpak-kcm"
pkgver = "6.2.4"
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
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE Flatpak permissions KCM"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/flatpak-kcm"
source = f"$(KDE_SITE)/plasma/{pkgver}/flatpak-kcm-{pkgver}.tar.xz"
sha256 = "10f8b218b32fd4d0837b17e8bf876e13666047c938fba23d77bdf409c3b23e83"
hardening = ["vis"]

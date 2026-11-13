pkgname = "flatpak-kcm"
pkgver = "6.8.3"
pkgrel = 0
build_style = "cmake"
# segfaults in libflatpak probably due to checking system-repo related stuff
# in chroot
make_check_args = ["-E", "flatpakpermissiontest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
sha256 = "3433d819c8bd449625ce90012317e47f669f23f91cdfdf28d5328024209a77b5"
hardening = ["vis"]

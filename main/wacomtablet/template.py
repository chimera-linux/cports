pkgname = "wacomtablet"
pkgver = "6.5.2"
pkgrel = 0
build_style = "cmake"
# X*: fail outside x11
make_check_args = ["-E", "(XInputAdaptor|XsetWacomAdaptor|DBusTabletService)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libplasma-devel",
    "libwacom-devel",
    "plasma5support-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "xserver-xorg-input-wacom-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "GUI configurator for Wacom tablets"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/wacomtablet"
source = f"$(KDE_SITE)/plasma/{pkgver}/wacomtablet-{pkgver}.tar.xz"
sha256 = "c00d59a37ad86d68a6f5f1120b09b4d946fa1cd8c48c575d6671f8566479bc63"

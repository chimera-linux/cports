pkgname = "kinfocenter"
pkgver = "6.1.3"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kirigami-addons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "libusb-devel",
    "qt6-qtbase-devel",
    # TODO: SeleniumWebDriverATSPI? (GUI accessibility tests)
]
depends = [
    "kdeclarative",
    "systemsettings",
]
pkgdesc = "Utility providing information about your system"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kinfocenter"
source = f"$(KDE_SITE)/plasma/{pkgver}/kinfocenter-{pkgver}.tar.xz"
sha256 = "69c4bebf97c5a980c3da57deedfff628254f03b7c094cca8d742f537bfc45738"
# symlink to systemsettings, runtime dep provided
broken_symlinks = ["usr/bin/kinfocenter"]
hardening = ["vis"]


@subpackage("kinfocenter-meta")
def _meta(self):
    self.subdesc = "recommends package"
    self.install_if = [self.parent]
    self.depends = [
        # basic
        "plasma-systemmonitor",
        # devices
        "libpulse-progs",
        "lscpu",
        "aha",
        "fwupd",
        "pciutils",
        # graphics
        "clinfo",
        "mesa-utils",
        "vulkan-tools",
        "wayland-utils",
        "qt6-qttools-qdbus",
        "xdpyinfo",
    ]
    self.options = ["empty"]
    if self.rparent.profile().arch in ["aarch64", "riscv64", "x86_64"]:
        self.depends += ["dmidecode"]

    return []

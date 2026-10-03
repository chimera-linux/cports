pkgname = "kinfocenter"
pkgver = "6.7.91"
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
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "libusb-devel",
    "qt6-qtbase-devel",
    "qt6-qtgraphs-devel",
    # TODO: SeleniumWebDriverATSPI? (GUI accessibility tests)
]
depends = ["kdeclarative", "qt6-qtgraphs", "systemsettings"]
pkgdesc = "Utility providing information about your system"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kinfocenter"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/kinfocenter-{pkgver}.tar.xz"
sha256 = "e8bc6e9f78cb97f6e901c24270a87991171d0b06009b48cd63e773400006ced1"
# symlink to systemsettings, runtime dep provided
broken_symlinks = ["usr/bin/kinfocenter"]
hardening = ["vis"]


@subpackage("kinfocenter-meta")
def _(self):
    self.subdesc = "recommends package"
    self.install_if = [self.parent]
    self.depends = [
        # basic
        "plasma-systemmonitor",
        # devices
        "libpulse-progs",
        "cmd:lscpu!util-linux-lscpu",
        "aha",
        "fwupd",
        "pciutils",
        "lm-sensors",
        # graphics
        "clinfo",
        "mesa-demos-core",
        "vulkan-tools",
        "wayland-utils",
        "qt6-qttools-qdbus",
        "xdpyinfo",
    ]
    self.options = ["empty"]
    if self.rparent.profile.arch in ["aarch64", "riscv64", "x86_64"]:
        self.depends += ["dmidecode"]

    return []

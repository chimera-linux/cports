pkgname = "kinfocenter"
pkgver = "6.1.0"
pkgrel = 2
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
sha256 = "283ca57849087bc61295d4905fe6bf68ff7c8b01830b87479fab9abc72db54de"
# symlink to systemsettings, runtime dep provided
broken_symlinks = ["usr/bin/kinfocenter"]
# FIXME: cfi kills app on launch in kcm_about-distro.so
hardening = ["vis", "!cfi"]


@subpackage("kinfocenter-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
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
        "qdbus",
        "xdpyinfo",
    ]
    self.options = ["empty"]
    if self.rparent.profile().arch in ["aarch64", "riscv64", "x86_64"]:
        self.depends += ["dmidecode"]

    return []

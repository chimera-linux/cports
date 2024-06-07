pkgname = "kinfocenter"
pkgver = "6.0.5"
pkgrel = 1
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
sha256 = "bf4f2c627242d827867306c4e884796c7d5f8a7a2a29444a494c2acad5c88973"
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
        "lscpu",
        "aha",
        "fwupd",
        "pciutils",
        # graphics
        "clinfo",
        "mesa-utils",
        "vulkan-tools",
        "wayland-utils",
        "qt6-qttools",  # FIXME: adds ~50 MiB, clang-libs heavy? split qt6-qttools into more subpkgs? just qdbus needed here
        "xdpyinfo",
    ]
    self.options = ["empty"]
    if self.rparent.profile().arch in ["aarch64", "riscv64", "x86_64"]:
        self.depends += ["dmidecode"]

    return []


# FIXME: kinfo stops midway through printing "Processors:" line, after nproc and right before "×"

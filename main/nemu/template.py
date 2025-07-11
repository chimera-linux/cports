pkgname = "nemu"
pkgver = "3.3.1"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DNM_WITH_DBUS=ON",
    "-DNM_WITH_NETWORK_MAP=ON",
    "-DNM_WITH_REMOTE=ON",
    "-DNM_WITH_USB=ON",
]
hostmakedepends = [
    "cmake",
    "gettext-devel",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "graphviz-devel",
    "json-c-devel",
    "libarchive-devel",
    "libusb-devel",
    "libxml2-devel",
    "linux-headers",
    "ncurses-devel",
    "sqlite-devel",
]
pkgdesc = "Ncurses UI for QEMU"
license = "BSD-2-Clause"
url = "https://github.com/nemuTUI/nemu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7cdb27cbf5df1957d0f0a258fc334f15d9e2d06a450a982bb796094efc3960c0"
tool_flags = {"CFLAGS": ["-Wno-strict-prototypes"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

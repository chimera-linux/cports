pkgname = "nemu"
pkgver = "3.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
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
sha256 = "dc251c6c478d60734a964324c028904e9da97dfeded7e5c6855f65e594e9a065"
tool_flags = {"CFLAGS": ["-Wno-strict-prototypes"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

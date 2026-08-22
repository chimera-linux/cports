pkgname = "htop"
pkgver = "3.5.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-capabilities",
    "--enable-delayacct",
    "--enable-sensors",
    "--enable-unicode",
]
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "libcap-devel",
    "libnl-devel",
    "lm-sensors-devel",
    "ncurses-devel",
]
depends = [
    # dlopened
    "so:libnl-3.so.200!libnl",
    "so:libnl-genl-3.so.200!libnl",
    "so:libsensors.so.5!lm-sensors-libs",
]
pkgdesc = "Interactive process viewer"
license = "GPL-2.0-only"
url = "https://htop.dev"
source = f"https://github.com/htop-dev/htop/releases/download/{pkgver}/htop-{pkgver}.tar.xz"
sha256 = "a8b164386494cb85bb255a415a3f5f80afe7a0c4491da5d113b3a0f951087e65"
# CFI cannot work with libsensors dlsym() stuff
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rename(
        "usr/share/pixmaps/htop.png",
        "usr/share/icons/hicolor/128x128/apps/htop.png",
        relative=False,
    )

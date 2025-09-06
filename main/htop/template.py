pkgname = "htop"
pkgver = "3.4.1"
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
sha256 = "904f7d4580fc11cffc7e0f06895a4789e0c1c054435752c151e812fead9f6220"
# CFI cannot work with libsensors dlsym() stuff
hardening = ["vis", "!cfi"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]

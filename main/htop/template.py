pkgname = "htop"
pkgver = "3.5.1"
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
sha256 = "526cecd62870aa8d14d2a79a35ea197e4e2b5317d275b567cee0574b2ddb2e9a"
# CFI cannot work with libsensors dlsym() stuff
hardening = ["vis", "!cfi"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]

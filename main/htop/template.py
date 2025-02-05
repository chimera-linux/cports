pkgname = "htop"
pkgver = "3.3.0"
pkgrel = 2
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
pkgdesc = "Interactive process viewer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://htop.dev"
source = f"https://github.com/htop-dev/htop/releases/download/{pkgver}/htop-{pkgver}.tar.xz"
sha256 = "a69acf9b42ff592c4861010fce7d8006805f0d6ef0e8ee647a6ee6e59b743d5c"
# CFI cannot work with libsensors dlsym() stuff
hardening = ["vis", "!cfi"]

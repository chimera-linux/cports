pkgname = "u-boot-pinebook-pro-rk3399"
pkgver = "2025.01"
pkgrel = 0
archs = ["aarch64"]
build_style = "u_boot"
make_build_args = [
    "BL31="
    + str(
        self.profile().sysroot / "usr/lib/trusted-firmware-a/rk3399/bl31.elf"
    ),
]
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-aarch64-none-elf",
    "gnutls-devel",
    "libuuid-devel",
    "openssl-devel",
    "python-devel",
    "python-pyelftools",
    "python-setuptools",
    "swig",
]
makedepends = ["atf-rk3399-bl31"]
pkgdesc = "U-Boot for Pinebook Pro"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "cdef7d507c93f1bbd9f015ea9bc21fa074268481405501945abc6f854d5b686f"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "idbloader.img u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]

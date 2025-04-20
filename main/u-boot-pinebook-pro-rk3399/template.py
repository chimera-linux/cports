pkgname = "u-boot-pinebook-pro-rk3399"
pkgver = "2025.04"
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
    "openssl3-devel",
    "python-devel",
    "python-pyelftools",
    "python-setuptools",
    "swig",
    "util-linux-uuid-devel",
]
makedepends = ["atf-rk3399-bl31"]
pkgdesc = "U-Boot for Pinebook Pro"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "439d3bef296effd54130be6a731c5b118be7fddd7fcc663ccbc5fb18294d8718"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "idbloader.img:64 u-boot.itb:16384",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]

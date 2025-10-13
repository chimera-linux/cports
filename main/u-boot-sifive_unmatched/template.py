pkgname = "u-boot-sifive_unmatched"
pkgver = "2025.10"
pkgrel = 0
archs = ["riscv64"]
build_style = "u_boot"
make_build_args = ["OPENSBI=/usr/lib/opensbi/generic/fw_dynamic.bin"]
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "gnutls-devel",
    "opensbi",
    "openssl3-devel",
    "python-devel",
    "python-setuptools",
    "swig",
    "util-linux-uuid-devel",
]
pkgdesc = "U-Boot for HiFive Unmatched boards"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "b4f032848e56cc8f213ad59f9132c084dbbb632bc29176d024e58220e0efdf4a"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin:34 u-boot.itb:2082",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

pkgname = "u-boot-qemu-riscv64"
pkgver = "2025.10"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "gnutls-devel",
    "openssl3-devel",
    "python-setuptools",
    "util-linux-uuid-devel",
]
pkgdesc = "U-Boot for qemu-riscv64"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "b4f032848e56cc8f213ad59f9132c084dbbb632bc29176d024e58220e0efdf4a"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

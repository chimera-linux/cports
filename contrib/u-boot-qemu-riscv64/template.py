pkgname = "u-boot-qemu-riscv64"
pkgver = "2023.04"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "gmake",
    "gcc-riscv64-unknown-elf",
    "flex",
    "bison",
    "dtc",
    "python-setuptools",
    "openssl-devel",
]
pkgdesc = "U-Boot for qemu-riscv64"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "e31cac91545ff41b71cec5d8c22afd695645cd6e2a442ccdacacd60534069341"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

pkgname = "u-boot-qemu-riscv64_smode"
pkgver = "2024.07"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "openssl-devel",
    "python-setuptools",
]
pkgdesc = "U-Boot for qemu-riscv64 supervisor mode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "f591da9ab90ef3d6b3d173766d0ddff90c4ed7330680897486117df390d83c8f"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

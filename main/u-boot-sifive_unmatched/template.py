pkgname = "u-boot-sifive_unmatched"
pkgver = "2024.07"
pkgrel = 0
archs = ["riscv64"]
build_style = "u_boot"
make_build_args = ["OPENSBI=/usr/lib/opensbi/generic/fw_dynamic.bin"]
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "opensbi",
    "openssl-devel",
    "python-devel",
    "python-setuptools",
    "swig",
]
pkgdesc = "U-Boot for HiFive Unmatched boards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "f591da9ab90ef3d6b3d173766d0ddff90c4ed7330680897486117df390d83c8f"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

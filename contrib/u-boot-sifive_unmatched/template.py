pkgname = "u-boot-sifive_unmatched"
pkgver = "2023.04"
pkgrel = 0
archs = ["riscv64"]
build_style = "u_boot"
make_build_args = ["OPENSBI=/usr/lib/opensbi/generic/fw_dynamic.bin"]
hostmakedepends = [
    "gmake", "gcc-riscv64-unknown-elf", "flex", "bison", "dtc", "swig",
    "opensbi", "python-devel", "openssl-devel", "python-setuptools",
]
pkgdesc = "U-Boot for HiFive Unmatched boards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "e31cac91545ff41b71cec5d8c22afd695645cd6e2a442ccdacacd60534069341"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

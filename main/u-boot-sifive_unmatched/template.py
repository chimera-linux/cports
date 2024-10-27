pkgname = "u-boot-sifive_unmatched"
pkgver = "2024.10"
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
    "libuuid-devel",
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
sha256 = "b28daf4ac17e43156363078bf510297584137f6df50fced9b12df34f61a92fb0"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

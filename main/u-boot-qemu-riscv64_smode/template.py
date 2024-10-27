pkgname = "u-boot-qemu-riscv64_smode"
pkgver = "2024.10"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "gnutls-devel",
    "libuuid-devel",
    "openssl-devel",
    "python-setuptools",
]
pkgdesc = "U-Boot for qemu-riscv64 supervisor mode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "b28daf4ac17e43156363078bf510297584137f6df50fced9b12df34f61a92fb0"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

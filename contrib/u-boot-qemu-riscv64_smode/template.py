pkgname = "u-boot-qemu-riscv64_smode"
pkgver = "2022.10"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "gmake", "gcc-riscv64-unknown-elf", "flex", "bison",
    "dtc", "python", "openssl-devel"
]
pkgdesc = "U-Boot for qemu-riscv64 supervisor mode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "50b4482a505bc281ba8470c399a3c26e145e29b23500bc35c50debd7fa46bdf8"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

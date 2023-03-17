pkgname = "u-boot-qemu_arm64"
pkgver = "2023.01"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "gmake", "gcc-aarch64-none-elf", "flex", "bison",
    "dtc", "python", "openssl-devel"
]
pkgdesc = "U-Boot for qemu-aarch64"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "69423bad380f89a0916636e89e6dcbd2e4512d584308d922d1039d1e4331950f"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

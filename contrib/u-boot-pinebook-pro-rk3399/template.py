# CAUTION: 2022.07 has SD card issues in Linux (the SD
# card does not init and we fall back to initramfs shell)
pkgname = "u-boot-pinebook-pro-rk3399"
pkgver = "2022.04"
pkgrel = 0
archs = ["aarch64"]
build_style = "u_boot"
make_build_args = [
    "BL31=" + str(self.profile().sysroot / "usr/lib/trusted-firmware-a/rk3399/bl31.elf"),
]
hostmakedepends = [
    "gmake", "gcc-aarch64-none-elf", "flex", "bison",
    "dtc", "python", "openssl-devel"
]
makedepends = ["atf-rk3399-bl31"]
pkgdesc = "U-Boot for Pinebook Pro"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "68e065413926778e276ec3abd28bb32fa82abaa4a6898d570c1f48fbdb08bcd0"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "idbloader.img u-boot.itb",
}
hardening = ["!vis", "!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]

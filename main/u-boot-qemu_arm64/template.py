pkgname = "u-boot-qemu_arm64"
pkgver = "2026.10"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "bash",
    "bison",
    "dtc",
    "flex",
    "gcc-aarch64-none-elf",
    "gnutls-devel",
    "openssl3-devel",
    "python-setuptools",
    "util-linux-uuid-devel",
]
pkgdesc = "U-Boot for qemu-aarch64"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://git.u-boot-project.org/u-boot/u-boot/-/releases/v{pkgver}/downloads/u-boot-{pkgver}.tar.bz2"
sha256 = "3f856da3cbbc93af51ff95fde18588a348b4a26723b01d9841e999d988481015"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]

pkgname = "u-boot-sifive_unmatched"
pkgver = "2022.10"
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
sha256 = "50b4482a505bc281ba8470c399a3c26e145e29b23500bc35c50debd7fa46bdf8"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin u-boot.itb",
}
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

pkgname = "u-boot-imx8mq_reform2"
pkgver = "2018.07"
pkgrel = 0
_commit = "4d563c4525e1500c0633abfb2b90ba8ad846dd91"
archs = ["aarch64"]
build_style = "u_boot"
make_build_args = ["u-boot.bin", "flash.bin"]
hostmakedepends = [
    "gmake", "gcc-aarch64-none-elf", "flex", "bison",
    "dtc", "python", "openssl-devel"
]
pkgdesc = "U-Boot for MNT Reform 2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://source.mnt.re/reform/reform-boundary-uboot"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "deb9c9c9e4ae8ac71798144f55add574c5b84bbdaa70e52827065977fd95e08d"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin u-boot.itb flash.bin",
}
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]

def do_configure(self):
    self.cp("mntreform-config", ".config")

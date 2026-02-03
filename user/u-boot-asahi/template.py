# make sure to also change update.py
pkgname = "u-boot-asahi"
pkgver = "2025.04"
pkgrel = 0
_asahiver = 1
archs = ["aarch64"]
build_style = "u_boot"
hostmakedepends = [
    "bison",
    "flex",
    "gcc-aarch64-none-elf",
]
makedepends = [
    "gnutls-devel",
    "openssl3-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "U-Boot for Apple Silicon"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://github.com/AsahiLinux/u-boot"
source = f"https://github.com/AsahiLinux/u-boot/archive/refs/tags/asahi-v{pkgver}-{_asahiver}.tar.gz"
sha256 = "82d21cbaf94d1212d6f1a851931d25163ed5e6247b9e60db8d39a3cf238dfd43"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]


def configure(self):
    self.do(
        "env",
        "-u",
        "CFLAGS",
        "-u",
        "CXXFLAGS",
        "-u",
        "CPPFLAGS",
        "-u",
        "LDFLAGS",
        "--",
        "make",
        "apple_m1_defconfig",
        f"CROSS_COMPILE={self.env['U_BOOT_TRIPLET']}-",
        f"CC={self.env['U_BOOT_TRIPLET']}-gcc",
        *self.configure_args,
    )


def install(self):
    self.install_file("u-boot-nodtb.bin", "usr/lib/asahi-boot")
    self.install_file(
        "arch/arm/dts/t[86]*.dtb", "usr/lib/asahi-boot/dtb", glob=True
    )
    for f in (self.cwd / "Licenses").iterdir():
        self.install_license(f"Licenses/{f.name}")

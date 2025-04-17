# make sure to also change update.py
pkgname = "u-boot-asahi"
pkgver = "2024.10"
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
sha256 = "c226191d52d3f853dd7d4e2c241e4259b90bd0aecb4c56e324936cc61b1bb53e"
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

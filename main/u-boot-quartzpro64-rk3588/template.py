pkgname = "u-boot-quartzpro64-rk3588"
pkgver = "2025.10"
pkgrel = 0
archs = ["aarch64"]
build_style = "u_boot"
make_build_args = [
    "BL31="
    + str(
        self.profile().sysroot / "usr/lib/trusted-firmware-a/rk3588/bl31.elf"
    ),
]
hostmakedepends = [
    "bash",
    "bison",
    "dtc",
    "flex",
    "gcc-aarch64-none-elf",
    "gnutls-devel",
    "openssl3-devel",
    "python-devel",
    "python-pyelftools",
    "python-setuptools",
    "swig",
    "util-linux-uuid-devel",
]
makedepends = ["atf-rk3588-bl31"]
pkgdesc = "U-Boot for QuartzPro64"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
_ddr_ver = "1.18"
source = [
    f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2",
    f"!https://github.com/rockchip-linux/rkbin/raw/refs/heads/master/bin/rk35/rk3588_ddr_lp4_2112MHz_lp5_2400MHz_v{_ddr_ver}.bin>ddr-v{_ddr_ver}.bin",
]
sha256 = [
    "b4f032848e56cc8f213ad59f9132c084dbbb632bc29176d024e58220e0efdf4a",
    "d89d40a8183b099589bfcffc5cc2ce9d874eb5b1d19b78bdad2cfcf45b9cb68f",
]
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "idbloader.img:64 u-boot.itb:16384",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]


def post_extract(self):
    self.cp(self.sources_path / f"ddr-v{_ddr_ver}.bin", ".")


def init_build(self):
    self.make_build_args += [f"ROCKCHIP_TPL=ddr-v{_ddr_ver}.bin"]

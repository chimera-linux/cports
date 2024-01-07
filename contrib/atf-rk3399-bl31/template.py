pkgname = "atf-rk3399-bl31"
pkgver = "2.8.11"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "gcc-aarch64-none-elf", "gcc-arm-none-eabi"]
pkgdesc = "ARM Trusted Firmware for Rockchip rk3399 boards (bl31)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://developer.trustedfirmware.org/dashboard/view/6"
source = f"https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git/snapshot/trusted-firmware-a-lts-v{pkgver}.tar.gz"
sha256 = "7b061acf0696df4a9f6cbeeb485ed9d875275a9dd426293ef572e5060dc6af10"
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "execstack"]


def do_build(self):
    # we undef all the stuff cbuild automatically sets,
    # and always "cross compile" with our bare metal toolchain
    self.do(
        "env",
        "-u",
        "CFLAGS",
        "-u",
        "LDFLAGS",
        "-u",
        "CPPFLAGS",
        "-u",
        "CXXFLAGS",
        "--",
        "gmake",
        f"-j{self.make_jobs}",
        "PLAT=rk3399",
        "bl31",
        "CROSS_COMPILE=aarch64-none-elf-",
        "CC=aarch64-none-elf-gcc",
    )


def do_install(self):
    self.install_file(
        "build/rk3399/release/bl31/bl31.elf",
        "usr/lib/trusted-firmware-a/rk3399",
        mode=0o755,
    )
    self.install_license("docs/license.rst")

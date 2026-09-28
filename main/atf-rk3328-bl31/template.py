pkgname = "atf-rk3328-bl31"
pkgver = "2.12.6"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
hostmakedepends = ["gcc-aarch64-none-elf", "gcc-arm-none-eabi"]
pkgdesc = "ARM Trusted Firmware for Rockchip rk3328 boards"
subdesc = "bl31"
license = "BSD-3-Clause"
url = "https://developer.trustedfirmware.org/dashboard/view/6"
# unstable tarball checksum
# source = f"https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+archive/refs/tags/lts-v{pkgver}.tar.gz"
source = f"https://ftp.octaforge.org/q66/random/lts-v{pkgver}.tar.gz"
sha256 = "bc709b5a795de3bd1c42e2a0b98c9dfb99cafb0bc6a49a1c90eca59ef541802b"
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "execstack"]


def build(self):
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
        "make",
        f"-j{self.make_jobs}",
        "PLAT=rk3328",
        "bl31",
        "CROSS_COMPILE=aarch64-none-elf-",
        "CC=aarch64-none-elf-gcc",
        "AS=aarch64-none-elf-gcc",
        "CPP=aarch64-none-elf-cpp",
    )


def install(self):
    self.install_file(
        "build/rk3328/release/bl31/bl31.elf",
        "usr/lib/trusted-firmware-a/rk3328",
        mode=0o755,
    )
    self.install_license("docs/license.rst")

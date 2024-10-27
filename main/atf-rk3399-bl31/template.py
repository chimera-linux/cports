pkgname = "atf-rk3399-bl31"
pkgver = "2.10.9"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
hostmakedepends = ["gcc-aarch64-none-elf", "gcc-arm-none-eabi"]
pkgdesc = "ARM Trusted Firmware for Rockchip rk3399 boards"
subdesc = "bl31"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://developer.trustedfirmware.org/dashboard/view/6"
# unstable tarball checksum
# source = f"https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+archive/refs/tags/lts-v{pkgver}.tar.gz"
source = f"https://ftp.octaforge.org/q66/random/lts-v{pkgver}.tar.gz"
sha256 = "e51985284ee515c54ecad21d6686354490a64e6380112a1bbf5d864638433e42"
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
        "PLAT=rk3399",
        "bl31",
        "CROSS_COMPILE=aarch64-none-elf-",
        "CC=aarch64-none-elf-gcc",
    )


def install(self):
    self.install_file(
        "build/rk3399/release/bl31/bl31.elf",
        "usr/lib/trusted-firmware-a/rk3399",
        mode=0o755,
    )
    self.install_license("docs/license.rst")

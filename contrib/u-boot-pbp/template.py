pkgname = "u-boot-pbp"
pkgver = "2022.07"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
make_cmd = "gmake"
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
sha256 = "92b08eb49c24da14c1adbf70a71ae8f37cc53eeb4230e859ad8b6733d13dcf5e"
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]

def do_configure(self):
    self.do(
        "env", "-u", "CFLAGS", "-u", "CXXFLAGS",
        "-u", "CPPFLAGS", "-u", "LDFLAGS",
        "gmake", "pinebook-pro-rk3399_defconfig",
        "CC=aarch64-none-elf-gcc",
    )

def do_build(self):
    bl31 = self.profile().sysroot / "usr/lib/trusted-firmware-a/rk3399/bl31.elf"
    # we undef all the stuff cbuild automatically sets,
    # and always "cross compile" with our bare metal toolchain
    self.do(
        "env", "-u", "CFLAGS", "-u", "LDFLAGS",
        "-u", "CPPFLAGS", "-u", "CXXFLAGS", "--",
        "gmake", f"-j{self.make_jobs}",
        f"EXTRAVERSION=-{pkgrel}", f"BL31={bl31}",
        "CROSS_COMPILE=aarch64-none-elf-",
        "CC=aarch64-none-elf-gcc",
    )

def do_install(self):
    destp = "usr/lib/u-boot/pbp-rk3399"
    for f in [
        "idbloader.img", "u-boot.itb", ".config",
    ]:
        self.install_file(f, destp)
    # licenses
    for f in [
        "Exceptions", "OFL.txt", "README", "bsd-2-clause.txt",
        "bsd-3-clause.txt", "eCos-2.0.txt", "gpl-2.0.txt",
        "ibm-pibs.txt", "isc.txt", "lgpl-2.0.txt", "lgpl-2.1.txt",
        "r8a779x_usb3.txt", "x11.txt",
    ]:
        self.install_license(f"Licenses/{f}")

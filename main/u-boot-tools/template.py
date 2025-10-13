pkgname = "u-boot-tools"
pkgver = "2025.10"
pkgrel = 0
build_style = "makefile"
make_build_target = "tools-all"
make_build_args = [
    "tools-only",
    "envtools",
    "HOSTSTRIP=:",
    "STRIP=:",
    "NO_SDL=1",
]
hostmakedepends = [
    "bison",
    "flex",
    "python",
    "python-devel",
    "python-setuptools",
    "swig",
]
makedepends = [
    "gnutls-devel",
    "linux-headers",
    "ncurses-libtinfo-devel",
    "openssl3-devel",
    "python-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Das U-Boot tools"
license = "GPL-2.0-or-later"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "b4f032848e56cc8f213ad59f9132c084dbbb632bc29176d024e58220e0efdf4a"
hardening = ["vis", "cfi"]
# weird test suite
options = ["!check"]

if self.profile().cross:
    make_build_args += [
        "CROSS_BUILD_TOOLS=y",
        f"CROSS_COMPILE={self.profile().triplet}-",
    ]


def configure(self):
    tcfl = self.get_cflags(shell=True)
    tlfl = self.get_ldflags(shell=True)
    tcc = self.get_tool("CC")
    with self.profile("host"):
        hcfl = self.get_cflags(shell=True)
        hlfl = self.get_ldflags(shell=True)
        hcc = self.get_tool("CC")

    self.make.invoke(
        "tools-only_defconfig",
        [
            "CC=" + tcc,
            "HOSTCC=" + hcc,
            "CFLAGS=" + tcfl,
            "HOSTCFLAGS=" + hcfl,
            "LDFLAGS=" + tlfl,
            "HOSTLDFLAGS=" + hlfl,
        ],
    )


def install(self):
    for t in [
        "dumpimage",
        "fdtgrep",
        "fit_check_sign",
        "fit_info",
        "gen_eth_addr",
        "gen_ethaddr_crc",
        "ifwitool",
        "img2srec",
        "mkeficapsule",
        "mkenvimage",
        "mkimage",
        "proftool",
        "spl_size_limit",
        "env/fw_printenv",
    ]:
        self.install_bin(f"tools/{t}")
    # extras
    self.install_link("usr/bin/fw_setenv", "fw_printenv")

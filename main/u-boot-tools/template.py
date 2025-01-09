pkgname = "u-boot-tools"
pkgver = "2025.01"
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
    "swig",
    "python-devel",
    "python-setuptools",
]
makedepends = [
    "openssl-devel",
    "linux-headers",
    "libuuid-devel",
    "gnutls-devel",
    "ncurses-libtinfo-devel",
    "python-devel",
]
pkgdesc = "Das U-Boot tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "cdef7d507c93f1bbd9f015ea9bc21fa074268481405501945abc6f854d5b686f"
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

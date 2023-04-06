pkgname = "u-boot-tools"
pkgver = "2023.04"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "tools-all"
make_build_args = [
    "tools-only", "envtools", "HOSTSTRIP=:", "STRIP=:", "NO_SDL=1"
]
hostmakedepends = [
    "gmake", "bison", "flex", "python", "swig", "python-setuptools"
]
makedepends = [
    "openssl-devel", "linux-headers", "libuuid-devel", "gnutls-devel",
    "ncurses-libtinfo-devel", "python-devel",
]
pkgdesc = "Das U-Boot tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "e31cac91545ff41b71cec5d8c22afd695645cd6e2a442ccdacacd60534069341"
hardening = ["vis", "cfi"]
# weird test suite
options = ["!check"]

if self.profile().cross:
    make_build_args += [
        "CROSS_BUILD_TOOLS=y",
        f"CROSS_COMPILE={self.profile().triplet}-"
    ]

def do_configure(self):
    tcfl = self.get_cflags(shell = True)
    tlfl = self.get_ldflags(shell = True)
    tcc = self.get_tool("CC")
    with self.profile("host"):
        hcfl = self.get_cflags(shell = True)
        hlfl = self.get_ldflags(shell = True)
        hcc = self.get_tool("CC")

    self.make.invoke("tools-only_defconfig", [
        "CC=" + tcc,
        "HOSTCC=" + hcc,
        "CFLAGS=" + tcfl,
        "HOSTCFLAGS=" + hcfl,
        "LDFLAGS=" + tlfl,
        "HOSTLDFLAGS=" + hlfl,
    ])

def post_build(self):
    self.ln_s("fw_printenv", "tools/env/fw_setenv")

def do_install(self):
    for t in [
        "dumpimage", "fdtgrep", "fit_check_sign", "fit_info",
        "gen_eth_addr", "gen_ethaddr_crc", "ifwitool", "img2srec",
        "mkeficapsule", "mkenvimage", "mkimage", "proftool",
        "spl_size_limit", "env/fw_printenv", "env/fw_setenv",
    ]:
        self.install_bin(f"tools/{t}")

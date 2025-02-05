pkgname = "pciutils"
pkgver = "3.13.0"
pkgrel = 2
build_style = "makefile"
make_dir = "."
make_build_args = [
    f"HOST={self.profile().arch}-linux",
    "ZLIB=yes",
    "SHARED=yes",
    "SHAREDIR=/usr/share/hwdata",
    "MANDIR=/usr/share/man",
    "PREFIX=/usr",
]
make_install_args = [
    "SHARED=yes",
    "SHAREDIR=/usr/share/hwdata",
    "SBINDIR=/usr/bin",
    "MANDIR=/usr/share/man",
    "PREFIX=/usr",
]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel", "kmod-devel", "linux-headers"]
depends = ["hwdata-pci"]
pkgdesc = "PCI bus utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://mj.ucw.cz/sw/pciutils"
source = f"https://github.com/pciutils/pciutils/archive/v{pkgver}.tar.gz"
sha256 = "861fc26151a4596f5c3cb6f97d6c75c675051fa014959e26fb871c8c932ebc67"
# no check target
# ld: error: undefined symbol: pci_alloc ... and so on
options = ["!check", "!lto"]


def init_build(self):
    self.make_build_args += [
        "CC=" + self.get_tool("CC"),
        "OPT=" + self.get_cflags(shell=True),
    ]


def pre_build(self):
    self.make.build(["SHARED=no"])
    self.mv("lib/libpci.a", "libpci_a")
    self.make.invoke("clean")


def install(self):
    self.make.install(["install-lib", "STRIP="])
    # static lib
    self.install_file("libpci_a", "usr/lib", name="libpci.a")
    # provided by hwdata-pci
    self.uninstall("usr/share/hwdata")
    # we don't want to touch pci.ids
    self.uninstall("usr/bin/update-pciids")
    self.uninstall("usr/share/man/man8/update-pciids.8")


@subpackage("pciutils-devel")
def _(self):
    return self.default_devel(man="37")

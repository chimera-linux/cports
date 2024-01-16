pkgname = "pciutils"
pkgver = "3.10.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
make_build_args = [
    f"HOST={self.profile().arch}-linux",
    "ZLIB=yes",
    "SHARED=yes",
    "SHAREDIR=/usr/share/hwdata",
    "MANDIR=/usr/share/man",
]
make_install_args = [
    "SHARED=yes",
    "SHAREDIR=/usr/share/hwdata",
    "SBINDIR=/usr/bin",
    "MANDIR=/usr/share/man",
]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel", "libkmod-devel", "linux-headers"]
depends = ["hwdata-pci"]
pkgdesc = "PCI bus utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://mj.ucw.cz/pciutils.html"
source = f"https://github.com/pciutils/pciutils/archive/v{pkgver}.tar.gz"
sha256 = "e579d87f1afe2196db7db648857023f80adb500e8194c4488c8b47f9a238c1c6"
# no check target
# ld: error: undefined symbol: pci_alloc ... and so on
options = ["!check", "!lto"]


def pre_build(self):
    self.make.build(
        [
            "SHARED=no",
            "CC=" + self.get_tool("CC"),
            "CFLAGS=" + self.get_cflags(shell=True),
        ]
    )
    self.mv("lib/libpci.a", "libpci_a")
    self.make.invoke("clean")


def do_install(self):
    self.make.install(["install-lib", "PREFIX=/usr", "STRIP="])
    # static lib
    self.install_file("libpci_a", "usr/lib", name="libpci.a")
    # fix permissions
    (self.destdir / f"usr/lib/libpci.so.{pkgver}").chmod(0o755)
    # provided by hwdata-pci
    self.rm(self.destdir / "usr/share/hwdata", recursive=True)
    # we don't want to touch pci.ids
    self.rm(self.destdir / "usr/bin/update-pciids")
    self.rm(self.destdir / "usr/share/man/man8/update-pciids.8")


@subpackage("pciutils-devel")
def _devel(self):
    return self.default_devel(man="37")

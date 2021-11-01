pkgname = "hwids"
pkgver = "20210613"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["UDEV=yes"]
make_install_args = [
    "UDEV=yes", f"DOCDIR=/usr/share/doc/{pkgname}-{pkgver}",
    "MISCDIR=/usr/share/hwdata", "HWDBDIR=/usr/lib/udev/hwdb.d"
]
hostmakedepends = ["gmake", "eudev"]
makedepends = ["eudev-devel"]
depends = [
    f"hwids-usb={pkgver}-r{pkgrel}",
    f"hwids-pci={pkgver}-r{pkgrel}",
    f"hwids-net={pkgver}-r{pkgrel}",
    f"hwids-udev={pkgver}-r{pkgrel}"
]
pkgdesc = "Hardware identification databases"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause OR GPL-2.0-or-later"
url = "https://github.com/gentoo/hwids"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "e28f1787290e9ea17426aa4090bbf6aca9bbc9e6cd14da232778bfaef4938bc1"
# no test suite
options = ["!check"]

@subpackage("hwids-usb")
def _usb(self):
    self.pkgdesc = f"{pkgdesc} (USB IDs)"
    return ["usr/share/hwdata/usb.ids"]

@subpackage("hwids-pci")
def _usb(self):
    self.pkgdesc = f"{pkgdesc} (PCI IDs)"
    return ["usr/share/hwdata/pci.ids"]

@subpackage("hwids-net")
def _usb(self):
    self.pkgdesc = f"{pkgdesc} (Networking OUIs)"
    return ["usr/share/hwdata/oui.txt", "usr/share/hwdata/iab.txt"]

@subpackage("hwids-udev")
def _usb(self):
    self.depends = [
        f"hwids-usb={pkgver}-r{pkgrel}",
        f"hwids-pci={pkgver}-r{pkgrel}",
        f"hwids-net={pkgver}-r{pkgrel}",
    ]
    self.install_if = [
        "eudev", f"hwids-pci={pkgver}-r{pkgrel}"
    ]
    self.pkgdesc = f"{pkgdesc} (udev integration)"
    return ["etc", "usr/lib"]

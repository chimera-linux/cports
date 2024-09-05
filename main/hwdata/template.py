pkgname = "hwdata"
pkgver = "0.387"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--datadir=/usr/share",
    "--disable-blacklist",
]
make_check_env = {"NO_DOCKER": "1"}
hostmakedepends = ["pkgconf"]
checkdepends = ["pciutils", "python", "bash"]
depends = [
    self.with_pkgver("hwdata-usb"),
    self.with_pkgver("hwdata-pci"),
    self.with_pkgver("hwdata-net"),
    self.with_pkgver("hwdata-pnp"),
]
pkgdesc = "Hardware identification databases"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/vcrhonek/hwdata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8c6be8f0863a8ff5c83b2c46aa525b503b30d42792ed57891c40849de543e1ee"
# cycle with pciutils, etc.
options = ["!check", "empty"]


@subpackage("hwdata-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()


@subpackage("hwdata-usb")
def _(self):
    self.subdesc = "USB IDs"
    return ["usr/share/hwdata/usb.ids"]


@subpackage("hwdata-pci")
def _(self):
    self.subdesc = "PCI IDs"
    return ["usr/share/hwdata/pci.ids"]


@subpackage("hwdata-net")
def _(self):
    self.subdesc = "Networking OUIs"
    return ["usr/share/hwdata/oui.txt", "usr/share/hwdata/iab.txt"]


@subpackage("hwdata-pnp")
def _(self):
    self.subdesc = "PnP IDs"
    return ["usr/share/hwdata/pnp.ids"]

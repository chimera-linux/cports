pkgname = "hwdata"
pkgver = "0.384"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--datadir=/usr/share",
    "--disable-blacklist",
]
make_cmd = "gmake"
make_check_env = {"NO_DOCKER": "1"}
hostmakedepends = ["gmake", "pkgconf"]
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
sha256 = "caa496a6203084ee3404c688a75ea05b4b10eec93340c503199647216127f347"
# cycle with pciutils, etc.
options = ["!check", "empty"]


@subpackage("hwdata-devel")
def _devel(self):
    self.depends = [self.parent]
    return self.default_devel()


@subpackage("hwdata-usb")
def _usb(self):
    self.subdesc = "USB IDs"
    return ["usr/share/hwdata/usb.ids"]


@subpackage("hwdata-pci")
def _pci(self):
    self.subdesc = "PCI IDs"
    return ["usr/share/hwdata/pci.ids"]


@subpackage("hwdata-net")
def _net(self):
    self.subdesc = "Networking OUIs"
    return ["usr/share/hwdata/oui.txt", "usr/share/hwdata/iab.txt"]


@subpackage("hwdata-pnp")
def _pnp(self):
    self.subdesc = "PnP IDs"
    return ["usr/share/hwdata/pnp.ids"]

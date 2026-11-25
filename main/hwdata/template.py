pkgname = "hwdata"
pkgver = "0.408"
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
license = "GPL-2.0-or-later"
url = "https://github.com/vcrhonek/hwdata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ac7c34efc5941d5cbf739a8f7f6c84b1c2edea493fd3fca10906ef64d7afd690"
# cycle with pciutils, etc.
options = ["!check", "empty"]


@split("devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()


@split("usb")
def _(self):
    self.subdesc = "USB IDs"
    return ["usr/share/hwdata/usb.ids"]


@split("pci")
def _(self):
    self.subdesc = "PCI IDs"
    return ["usr/share/hwdata/pci.ids"]


@split("net")
def _(self):
    self.subdesc = "Networking OUIs"
    return ["usr/share/hwdata/oui.txt", "usr/share/hwdata/iab.txt"]


@split("pnp")
def _(self):
    self.subdesc = "PnP IDs"
    return ["usr/share/hwdata/pnp.ids"]

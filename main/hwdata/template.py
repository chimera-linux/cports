pkgname = "hwdata"
pkgver = "0.373"
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
    f"hwdata-usb={pkgver}-r{pkgrel}",
    f"hwdata-pci={pkgver}-r{pkgrel}",
    f"hwdata-net={pkgver}-r{pkgrel}",
    f"hwdata-pnp={pkgver}-r{pkgrel}",
]
pkgdesc = "Hardware identification databases"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/vcrhonek/hwdata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0db28dc635d5059ad23d068d2e56ef5dc540f95bc813ea5a3c0f5d63b03d20d6"
# cycle with pciutils, etc.
options = ["!check"]


@subpackage("hwdata-devel")
def _dev(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()


@subpackage("hwdata-usb")
def _usb(self):
    self.pkgdesc = f"{pkgdesc} (USB IDs)"
    return ["usr/share/hwdata/usb.ids"]


@subpackage("hwdata-pci")
def _pci(self):
    self.pkgdesc = f"{pkgdesc} (PCI IDs)"
    return ["usr/share/hwdata/pci.ids"]


@subpackage("hwdata-net")
def _net(self):
    self.pkgdesc = f"{pkgdesc} (Networking OUIs)"
    return ["usr/share/hwdata/oui.txt", "usr/share/hwdata/iab.txt"]


@subpackage("hwdata-pnp")
def _pnp(self):
    self.pkgdesc = f"{pkgdesc} (PnP IDs)"
    return ["usr/share/hwdata/pnp.ids"]

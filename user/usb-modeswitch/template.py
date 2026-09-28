pkgname = "usb-modeswitch"
pkgver = "2.6.2"
_dataver = "20251207"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "SBINDIR=$(DESTDIR)/usr/bin",
    "UDEVDIR=$(DESTDIR)/usr/lib/udev",
    "RULESDIR=$(DESTDIR)/usr/lib/udev/rules.d",
    "ETCDIR=$(DESTDIR)/usr/share/etc",
]
# puts DESTDIR in PREFIX definition etc. so avoid overriding that...
make_use_env = True
hostmakedepends = [
    "pkgconf",
    "tcl",
]
makedepends = ["libusb-devel"]
depends = ["tcl"]
pkgdesc = "Tool to control multi-mode USB devices"
license = "GPL-2.0-or-later"
url = "https://www.draisberghof.de/usb_modeswitch"
source = [
    f"{url}/usb-modeswitch-{pkgver}.tar.bz2",
    # check date on updates
    f"{url}/usb-modeswitch-data-{_dataver}.tar.bz2",
]
source_paths = [".", "data"]
sha256 = [
    "f7abd337784a9d1bd39cb8a587518aff6f2a43d916145eafd80b1b8b7146db66",
    "0bb12d64aee5e467c31af61a53fb828ff7aa59c54a82ca85eeede4c5690bfa66",
]
# no tests
options = ["!check"]


def post_build(self):
    self.make.build(wrksrc="data")


def install(self):
    # don't let it pass PREFIX= like the build style
    self.make.install()
    self.make.install(wrksrc="data")

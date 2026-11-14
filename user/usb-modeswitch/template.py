pkgname = "usb-modeswitch"
pkgver = "2.6.3"
_dataver = "20261111"
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
    "cddb987af80eca5bc9c364dc0ccd0e2b788de4d28626d017277a48c06b0453b6",
    "221507574da7d11debdba94e40cf164b59fb8b19be1a3ecbec76e348b7a4fa73",
]
# no tests
options = ["!check"]


def post_build(self):
    self.make.build(wrksrc="data")


def install(self):
    # don't let it pass PREFIX= like the build style
    self.make.install()
    self.make.install(wrksrc="data")

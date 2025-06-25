pkgname = "pcsc-cyberjack"
pkgver = "3.99.5.16"
_sp = pkgver[pkgver.rfind(".") + 1 :]
_version = pkgver[: -len(_sp) - 1]
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-udev"]
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "libusb-devel",
    "pcsc-lite-devel",
    "udev-devel",
]
pkgdesc = "PCSC driver for cyberJack® smart card readers"
license = "GPL-2.0-only"
url = "https://help.reiner-sct.com/de/support/solutions/articles/101000480008"
source = f"https://support.reiner-sct.de/downloads/LINUX/V{_version}_SP{_sp}/pcsc-cyberjack-{_version}final.SP{_sp}.tar.bz2"
sha256 = "141489261c0d436be4b92f78faf240c32694426685413d9d50e3585feba5eb79"


def post_install(self):
    self.rm(
        ">/usr/lib/pcsc/drivers/libifd-cyberjack.bundle/Contents/Linux/libifd-cyberjack.a"
    )
    self.mkdir(f">/usr/share/examples/{pkgname}", parents=True)
    self.mv(">/etc/cyberjack.conf.default", f">/usr/share/examples/{pkgname}")

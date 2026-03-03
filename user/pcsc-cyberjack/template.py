pkgname = "pcsc-cyberjack"
pkgver = "3.99.5.17"
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
sha256 = "f1a8e15db3a4268b0d79c32a76195b34d79518bb891685443e253311f9e9d30a"


def post_install(self):
    self.rm(
        ">/usr/lib/pcsc/drivers/libifd-cyberjack.bundle/Contents/Linux/libifd-cyberjack.a"
    )
    self.mkdir(f">/usr/share/examples/{pkgname}", parents=True)
    self.mv(">/etc/cyberjack.conf.default", f">/usr/share/examples/{pkgname}")

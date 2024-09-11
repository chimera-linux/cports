pkgname = "lxsession"
pkgver = "0.5.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-buildin-clipboard",
    "--enable-buildin-polkit",
    "--enable-gtk3",
]
# build fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "polkit-devel",
]
pkgdesc = "Classic LXDE session manager"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxsession"
source = f"https://downloads.sourceforge.net/lxde/lxsession-{pkgver}.tar.xz"
sha256 = "e43e0d9c033095559ab57c8821c2b84fea58009d267db1324d32dca8bd4dbb46"


def pre_configure(self):
    self.rm("*.stamp", glob=True)

pkgname = "lxpanel"
pkgver = "0.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-alsa",
    "--enable-gtk3",
    "--enable-plugins-loading",
    "--with-plugins=all",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libcurl-devel",
    "libfm-devel",
    "libkeybinder3-devel",
    "libwnck-devel",
    "menu-cache",
    "startup-notification-devel",
    "wireless-tools-devel",
]
pkgdesc = "Lightweight X11 desktop panel for LXDE"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxpanel"
source = f"https://downloads.sourceforge.net/lxde/{pkgname}-{pkgver}.tar.xz"
sha256 = "1e318f57d7e36b61c23a504d03d2430c78dad142c1804451061f1b3ea5441ee8"


@subpackage("lxpanel-devel")
def _(self):
    return self.default_devel()

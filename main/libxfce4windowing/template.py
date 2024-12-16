pkgname = "libxfce4windowing"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-tests"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "wayland-progs",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libdisplay-info-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxrandr-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Xfce windowing abstraction library"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://docs.xfce.org/xfce/libxfce4windowing/start"
source = f"$(XFCE_SITE)/xfce/libxfce4windowing/{pkgver[:-2]}/libxfce4windowing-{pkgver}.tar.bz2"
sha256 = "56f29b1d79606fb00a12c83ef4ece12877d2b22bf1acaaff89537fbe8e939f68"
options = ["!cross"]


@subpackage("libxfce4windowing-devel")
def _(self):
    return self.default_devel()

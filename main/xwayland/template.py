pkgname = "xwayland"
pkgver = "24.1.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dipv6=true",
    "-Dxcsecurity=true",
    "-Ddri3=true",
    "-Dglamor=true",
    "-Dxvfb=false",
    "-Dxdmcp=false",
    "-Dxwayland_ei=socket",
    "-Dxkb_dir=/usr/share/X11/xkb",
    "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "dbus-devel",
    "font-util-devel",
    "libei-devel",
    "libepoxy-devel",
    "libtirpc-devel",
    "libxcb-devel",
    "libxcvt-devel",
    "libxfont2-devel",
    "libxkbfile-devel",
    "libxshmfence-devel",
    "mesa-devel",
    "nettle-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "xorgproto",
    "xtrans",
]
# check if this needs to be updated when updating
depends = ["xserver-xorg-protocol>=20180227"]
pkgdesc = "Xwayland X server"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/xwayland-{pkgver}/xserver-xwayland-{pkgver}.tar.gz"
sha256 = "27b2c92659eaf3fc3705998bcdc6a8a3953c990f83023069425343ac9a85ebe2"
hardening = ["!vis", "!cfi"]
# needs xtest repository
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/share/man/man1/Xserver.1")
    # provided by xserver-xorg-protocol
    self.uninstall("usr/lib/xorg/protocol.txt")


@subpackage("xwayland-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()

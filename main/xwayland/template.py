pkgname = "xwayland"
pkgver = "21.1.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dipv6=true", "-Dxcsecurity=true", "-Ddri3=true", "-Dglamor=true",
    "-Dxvfb=false", "-Dxdmcp=false", "-Dxwayland_eglstream=false",
    "-Dxkb_dir=/usr/share/X11/xkb", "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfont2-devel", "libxkbfile-devel", "libxshmfence-devel",
    "libxcb-devel", "wayland-devel", "wayland-protocols", "libtirpc-devel",
    "mesa-devel", "libepoxy-devel", "pixman-devel", "nettle-devel",
    "dbus-devel", "font-util-devel", "xorgproto", "xtrans",
]
depends = ["xserver-common"]
pkgdesc = "Xwayland X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/{pkgname}-{pkgver}/xserver-{pkgname}-{pkgver}.tar.gz"
sha256 = "fe9636403a54f76a23b7d5ea41242b080fd5ef37c6bf04eb1f413e76070bb48c"
# needs xtest repository
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("xserver-common")
def _common(self):
    self.pkgdesc = f"X11 server from X.org (common files)"

    return ["usr/lib/xorg/protocol.txt"]

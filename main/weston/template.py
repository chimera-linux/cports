pkgname = "weston"
pkgver = "10.0.0"
pkgrel = 0
build_style = "meson"
# pipewire requires 0.2 in this release
configure_args = [
    "-Dsystemd=false", "-Dlauncher-logind=false", "-Dlauncher-libseat=true",
    "-Dpipewire=false", "-Dremoting=false", "-Dbackend-rdp=false",
    "-Dbackend-drm-screencast-vaapi=true", "-Dcolor-management-colord=true",
    "-Dtest-junit-xml=false", "-Db_ndebug=false",
    "-Ddefault_library=shared",
]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "wayland-protocols"]
makedepends = [
    "libpng-devel", "libwebp-devel", "lcms2-devel", "pixman-devel",
    "mesa-devel", "pango-devel", "cairo-devel", "mtdev-devel",
    "libinput-devel", "libxcb-devel", "libxcursor-devel", "libxkbcommon-devel",
    "wayland-devel", "wayland-protocols", "libdrm-devel",
    "linux-pam-devel", "eudev-devel", "dbus-devel",
    "colord-devel", "glu-devel", "libva-devel", "libseat-devel",
]
checkdepends = ["mesa-dri", "xwayland"]
pkgdesc = "Reference implementation of a Wayland compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "5c23964112b90238bed39e5dd1e41cd71a79398813cdc3bbb15a9fdc94e547ae"

def post_install(self):
    self.install_license("COPYING")

@subpackage("weston-x11")
def _x11(self):
    self.depends = [f"weston={pkgver}-r{pkgrel}"]
    self.pkgdesc = f"{pkgdesc} (X11 backend)"

    return ["usr/lib/libweston*/x11-backend.so"]

@subpackage("weston-xwayland")
def _xwayland(self):
    self.depends = [f"weston={pkgver}-r{pkgrel}"]
    self.pkgdecs = f"{pkgdesc} (XWayland plugin)"

    return ["usr/lib/libweston*/xwayland.so"]

@subpackage("weston-colord")
def _colord(self):
    self.pkgdesc = f"{pkgdesc} (colord plugin)"

    return ["usr/lib/weston/cms-colord.so"]

@subpackage("weston-libs")
def _lib(self):
    return self.default_libs(extra = [f"usr/lib/libweston-10"])

@subpackage("weston-devel")
def _devel(self):
    return self.default_devel()

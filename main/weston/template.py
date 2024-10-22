pkgname = "weston"
pkgver = "14.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Dpipewire=true",
    "-Dremoting=false",
    "-Dbackend-rdp=false",
    "-Dbackend-vnc=false",
    "-Dbackend-drm-screencast-vaapi=true",
    "-Dcolor-management-lcms=true",
    "-Dtest-junit-xml=false",
    "-Ddefault_library=shared",
]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "wayland-protocols"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glu-devel",
    "lcms2-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libinput-devel",
    "libpng-devel",
    "libseat-devel",
    "libva-devel",
    "libwebp-devel",
    "libxcb-devel",
    "libxcursor-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "mesa-devel",
    "mtdev-devel",
    "pango-devel",
    "pipewire-devel",
    "pixman-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["xwayland"]
pkgdesc = "Reference implementation of a Wayland compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/weston/-/releases/{pkgver}/downloads/weston-{pkgver}.tar.xz"
sha256 = "a8150505b126a59df781fe8c30c8e6f87da7013e179039eb844a5bbbcc7c79b3"


def post_install(self):
    self.install_license("COPYING")


@subpackage("weston-x11")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "X11 backend"

    return ["usr/lib/libweston*/x11-backend.so"]


@subpackage("weston-xwayland")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "Xwayland plugin"

    return ["usr/lib/libweston*/xwayland.so"]


@subpackage("weston-libs")
def _(self):
    return self.default_libs(extra=[f"usr/lib/libweston-{pkgver[0:2]}"])


@subpackage("weston-devel")
def _(self):
    return self.default_devel()

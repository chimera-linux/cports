pkgname = "mutter"
pkgver = "44.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Degl_device=true",
    "-Dudev=true",
    "-Dnative_backend=true",
    "-Dintrospection=true",
    "-Dprofiler=false",
    "-Dtests=false",
    "-Dxwayland_path=/usr/bin/Xwayland",
    "-Dxwayland_initfd=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext",
    "libxcvt-progs",
    "xwayland",
]
makedepends = [
    "glib-devel",
    "graphene-devel",
    "gtk4-devel",
    "pango-devel",
    "cairo-devel",
    "fribidi-devel",
    "gsettings-desktop-schemas-devel",
    "gnome-settings-daemon-devel",
    "gnome-desktop-devel",
    "json-glib-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxtst-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxrender-devel",
    "libxi-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "libxinerama-devel",
    "libxau-devel",
    "libice-devel",
    "libsm-devel",
    "libxcb-devel",
    "libcanberra-devel",
    "dbus-devel",
    "mesa-devel",
    "wayland-protocols",
    "wayland-devel",
    "udev-devel",
    "elogind-devel",
    "libwacom-devel",
    "pipewire-devel",
    "libinput-devel",
    "startup-notification-devel",
    "colord-devel",
    "lcms2-devel",
    "at-spi2-core-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME X11 window manager, Wayland display server and compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/Mutter"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "185cbebf2150d3e450550e371bdb13a8b4db096978b14f99521e966eacc70551"
# libmutter crashes gnome-shell with some applications? FIXME debug
hardening = ["!int"]
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("mutter-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/mutter-12/*.gir"])

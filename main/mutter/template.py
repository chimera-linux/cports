pkgname = "mutter"
pkgver = "48.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddefault_library=shared",
    "-Degl_device=true",
    "-Dintrospection=true",
    "-Dnative_backend=true",
    "-Dprofiler=false",
    "-Dtests=disabled",
    "-Dudev=true",
    "-Dxwayland_initfd=disabled",
    "-Dxwayland_path=/usr/bin/Xwayland",
]
hostmakedepends = [
    "bash-completion",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxcvt-progs",
    "meson",
    "pkgconf",
    "python-argcomplete",
    "python-docutils",
    "xwayland",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "colord-devel",
    "dbus-devel",
    "elogind-devel",
    "fribidi-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gnome-settings-daemon-devel",
    "graphene-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "json-glib-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libice-devel",
    "libinput-devel",
    "libsm-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxau-devel",
    "libxcb-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "libxtst-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "startup-notification-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME X11 window manager, Wayland display server and compositor"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/Mutter"
source = f"$(GNOME_SITE)/mutter/{pkgver.split('.')[0]}/mutter-{pkgver}.tar.xz"
sha256 = "1189cf7e63cc87cfdd1f3a86e8f14d97c33d6a9da254f23e81655549b6c50d93"
# libmutter crashes gnome-shell with some applications? FIXME debug
hardening = ["!int"]
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("mutter-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/mutter-16/*.gir"])

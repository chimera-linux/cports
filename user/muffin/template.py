pkgname = "muffin"
pkgver = "6.6.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dcogl_tests=false",
    "-Dclutter_tests=false",
    "-Dcore_tests=false",
    "-Dprofiler=false",
    "-Dtests=false",
    "-Dxwayland_initfd=disabled",
    "-Dxwayland_path=/usr/bin/Xwayland",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxcvt-progs",
    "meson",
    "pkgconf",
    "xwayland",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "cinnamon-desktop-devel",
    "dbus-devel",
    "elogind-devel",
    "fribidi-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "graphene-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libcanberra-devel",
    "libdrm-devel",
    "libgudev-devel",
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
    "libxkbcommon-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxtst-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "startup-notification-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xkeyboard-config",
    "xwayland-devel",
]
depends = ["cinnamon-desktop", "xwayland"]
pkgdesc = "Window manager and compositor for the Cinnamon desktop"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = (
    f"https://github.com/linuxmint/muffin/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "af1aa8e68699895a841415c007c7f3f48efc06f07c50d219d30f8131a981248e"
# same as mutter, which crashes with int hardening
hardening = ["!int"]
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("muffin-devel")
def _(self):
    return self.default_devel()

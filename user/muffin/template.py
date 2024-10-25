pkgname = "muffin"
pkgver = "6.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "-Degl_device=true",
    "-Dinstalled_tests=true",
    "-Dtests=true",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "libxcvt-progs",
    "meson",
    "pkgconf",
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
    "libgbm-devel",
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
depends = ["cinnamon-settings-daemon"]
pkgdesc = "Window management library for the Cinnamon desktop"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = (
    f"https://github.com/linuxmint/muffin/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "889200ceb45334899e7568f1735ec2b15e1ae042d176821a0d45c524960bee0a"
hardening = ["vis"]
# Tests require its own GSettings schemas to be installed
options = ["!check", "!cross"]


@subpackage("muffin-devel")
def _(self):
    return self.default_devel()


@subpackage("muffin-tests")
def _(self):
    self.subdesc = "installed tests"

    return [
        "usr/lib/installed-tests",
        "usr/share/installed-tests",
        "usr/share/muffin",
    ]

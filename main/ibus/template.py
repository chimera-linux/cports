pkgname = "ibus"
pkgver = "1.5.28"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ui",
    "--enable-gtk3",
    "--enable-memconf",
    "--enable-dconf",
    "--enable-wayland",
    "--enable-emoji-dict",
    "--enable-unicode-dict",
    "--enable-introspection",
    "--enable-vala",
    "--enable-setup",
    "--disable-gtk2",
    "--disable-schemas-compile",
    "--disable-systemd-services",
]
make_cmd = "gmake"
make_dir = "."  # tests assume this
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "gmake",
    "pkgconf",
    "dconf",
    "python",
    "vala",
    "gtk-doc-tools",
    "gobject-introspection",
    "glib-devel",
    "gettext-tiny-devel",
    "python-gobject-devel",
    "unicode-cldr-common",
    "unicode-emoji",
    "unicode-character-database",
]
makedepends = [
    "dconf-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxtst-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "iso-codes",
]
checkdepends = ["xserver-xorg-xvfb", "fonts-dejavu-otf", "setxkbmap", "bash"]
depends = ["python-gobject", "iso-codes", "dbus-x11"]
pkgdesc = "Intelligent Input Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibus/ibus"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6c9ff3a7576c3d61264f386030f47ee467eb7298c8104367002986e008765667"
options = ["!cross"]


@subpackage("libibus")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("ibus-gtk3")
def _gtk3(self):
    self.pkgdesc = f"{pkgdesc} (Gtk+3 immodule)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gtk+3"]

    return ["usr/lib/gtk-3.0/3.0.0/immodules/im-ibus.so"]


@subpackage("ibus-wayland")
def _wayland(self):
    self.pkgdesc = f"{pkgdesc} (Wayland support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "wayland"]

    return ["usr/libexec/ibus-wayland"]


@subpackage("ibus-x11")
def _xorg(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "libx11"]

    return ["usr/libexec/ibus-x11"]


@subpackage("ibus-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])


configure_gen = []

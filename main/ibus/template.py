pkgname = "ibus"
pkgver = "1.5.25"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ui", "--enable-gtk3", "--enable-memconf", "--enable-dconf",
    "--enable-wayland", "--enable-emoji-dict", "--enable-unicode-dict",
    "--enable-introspection", "--enable-vala", "--enable-setup",
    "--disable-gtk2", "--disable-schemas-compile",
]
configure_env = {"MAKE": "gmake"}
make_cmd = "gmake"
make_dir = "." # tests assume this
hostmakedepends = [
    "gmake", "pkgconf", "dconf", "python", "vala", "gtk-doc-tools",
    "gobject-introspection", "glib-devel", "gettext-tiny-devel",
    "python-gobject-devel", "unicode-cldr-common", "unicode-emoji",
    "unicode-character-database",
]
makedepends = [
    "dconf-devel", "gtk+3-devel", "json-glib-devel", "libnotify-devel",
    "libx11-devel", "libxtst-devel", "libxkbcommon-devel", "wayland-devel",
    "iso-codes",
]
depends = ["python-gobject", "iso-codes", "dbus-x11"]
pkgdesc = "Intelligent Input Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibus/ibus"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "dea4f663c485267cc3313e40a0bc89b977c397e19644f8ab41df0e6eaec34330"
# TODO: verify cross; check needs a graphical environment (use xvfb?)
options = ["!cross", "!check"]

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
def _wayland(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "libx11"]

    return ["usr/libexec/ibus-x11"]

@subpackage("ibus-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/gtk-doc"])

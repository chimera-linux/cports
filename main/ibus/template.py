pkgname = "ibus"
pkgver = "1.5.30"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ui",
    "--enable-gtk3",
    "--enable-gtk4",
    "--enable-memconf",
    "--enable-dconf",
    "--enable-wayland",
    "--enable-emoji-dict",
    "--enable-unicode-dict",
    "--enable-introspection",
    "--enable-vala",
    "--enable-setup",
    # dbusmenu-glib
    "--disable-appindicator",
    "--disable-gtk2",
    "--disable-schemas-compile",
    "--disable-systemd-services",
]
make_dir = "."  # tests assume this
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "automake",
    "dconf",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "python",
    "python-gobject-devel",
    "unicode-character-database",
    "unicode-cldr-common",
    "unicode-emoji",
    "vala",
]
makedepends = [
    "dconf-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "iso-codes",
    "json-glib-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "libxtst-devel",
    "wayland-devel",
]
checkdepends = ["xwayland-run", "fonts-dejavu-otf", "setxkbmap", "bash"]
depends = ["python-gobject", "iso-codes", "dbus-x11"]
pkgdesc = "Intelligent Input Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibus/ibus"
source = f"{url}/releases/download/{pkgver}/ibus-{pkgver}.tar.gz"
sha256 = "05b84d4a45139face161596e5ade8e6c5da55cfaf6f194861da66516190f5b96"
# gtk3 can't handle seatless wayland displays
options = ["!cross", "!check"]


def post_extract(self):
    # for some magical reason, not having this makes it run vala on something
    # weird and behave as if appindicator isn't disabled (we've always had it disabled
    # since no libdbusmenu-glib)
    # so, just touch an empty file
    (self.cwd / "ui/gtk3/panel.vala").touch()


@subpackage("libibus")
def _(self):
    self.subdesc = "runtime library"

    return self.default_libs()


@subpackage("ibus-gtk3")
def _(self):
    self.subdesc = "Gtk+3 immodule"
    self.install_if = [self.parent, "gtk+3"]

    return ["usr/lib/gtk-3.0/3.0.0/immodules/im-ibus.so"]


@subpackage("ibus-gtk4")
def _(self):
    self.subdesc = "Gtk4 immodule"
    self.install_if = [self.parent, "gtk4"]

    return ["usr/lib/gtk-4.0/4.0.0/immodules/libim-ibus.so"]


@subpackage("ibus-wayland")
def _(self):
    self.subdesc = "Wayland support"
    self.install_if = [self.parent, "wayland"]

    return ["usr/libexec/ibus-wayland"]


@subpackage("ibus-x11")
def _(self):
    self.subdesc = "X11 support"
    self.install_if = [self.parent, "libx11"]

    return ["usr/libexec/ibus-x11"]


@subpackage("ibus-devel")
def _(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])

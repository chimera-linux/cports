pkgname = "ibus"
pkgver = "1.5.29"
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
make_cmd = "gmake"
make_dir = "."  # tests assume this
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "automake",
    "dconf",
    "gettext-devel",
    "glib-devel",
    "gmake",
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
checkdepends = ["weston", "fonts-dejavu-otf", "setxkbmap", "bash"]
depends = ["python-gobject", "iso-codes", "dbus-x11"]
pkgdesc = "Intelligent Input Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibus/ibus"
# they botched the number for this one https://github.com/ibus/ibus/issues/2584
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}-rc2.tar.gz"
sha256 = "3a27ed120485b2077c62e36e788c302f34544ceac3b3b9cda28b7418e8051415"
# gtk3 can't handle seatless wayland displays
options = ["!cross", "!check"]


def post_extract(self):
    # for some magical reason, not having this makes it run vala on something
    # weird and behave as if appindicator isn't disabled (we've always had it disabled
    # since no libdbusmenu-glib)
    # so, just touch an empty file
    (self.cwd / "ui/gtk3/panel.vala").touch()


@subpackage("libibus")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("ibus-gtk3")
def _gtk3(self):
    self.pkgdesc = f"{pkgdesc} (Gtk+3 immodule)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gtk+3"]

    return ["usr/lib/gtk-3.0/3.0.0/immodules/im-ibus.so"]


@subpackage("ibus-gtk4")
def _gtk4(self):
    self.pkgdesc = f"{pkgdesc} (Gtk4 immodule)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gtk4"]

    return ["usr/lib/gtk-4.0/4.0.0/immodules/libim-ibus.so"]


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

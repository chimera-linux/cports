pkgname = "libdbusmenu"
pkgver = "16.04.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-dumper",
    "--disable-static",
    "--enable-gtk",
    "--enable-tests",
]
make_check_wrapper = ["dbus-run-session", "--", "xvfb-run", "--"]
hostmakedepends = [
    "automake",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "atkmm-devel",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-devel",
    "gtk-doc-tools",
    "json-glib-devel",
    "vala-devel",
]
checkdepends = ["bash", "dbus-test-runner", "xserver-xorg-xvfb"]
pkgdesc = "Library for passing menus over DBus"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later"
url = "https://launchpad.net/libdbusmenu"
source = f"{url}/{pkgver[: pkgver.rfind('.')]}/{pkgver}/+download/libdbusmenu-{pkgver}.tar.gz"
sha256 = "b9cc4a2acd74509435892823607d966d424bd9ad5d0b00938f27240a1bfa878a"


@subpackage("libdbusmenu-gtk3")
def _(self):
    self.subdesc = "GTK+3"
    return [
        "usr/lib/girepository-1.0/DbusmenuGtk3-0.4.typelib",
        "usr/lib/libdbusmenu-gtk3.so.4*",
    ]


@subpackage("libdbusmenu-devel")
def _(self):
    return self.default_devel()

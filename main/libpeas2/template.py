pkgname = "libpeas2"
pkgver = "2.0.7"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dvapi=true"]
make_check_args = ["--timeout-multiplier=5"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "lua5.1-lgi",
    "meson",
    "pkgconf",
    "python",
    "vala",
]
makedepends = [
    "gjs-devel",
    "glib-devel",
    "gtk+3-devel",
    "lua5.1-devel",
    "mozjs140-devel",
    "python-devel",
    "python-gobject-devel",
]
checkdepends = ["xwayland-run", "fonts-dejavu-ttf"]
pkgdesc = "GObject application plugin library 2.x"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Libpeas"
source = f"$(GNOME_SITE)/libpeas/{pkgver[:-2]}/libpeas-{pkgver}.tar.xz"
sha256 = "1e9a9d69761d2109eff5b7c11d8c96b4867ccfaca2b921eded49401192769ec9"
# fails
options = ["!cross"]


@subpackage("libpeas2-devel")
def _(self):
    return self.default_devel()


@subpackage("libpeas2-python")
def _(self):
    self.subdesc = "Python support"
    self.depends += ["python-gobject"]
    self.install_if = [self.parent, "python"]
    return ["usr/lib/libpeas-2/loaders/libpythonloader.so"]


@subpackage("libpeas2-lua")
def _(self):
    self.subdesc = "Lua 5.1 support"
    self.depends += ["lua5.1-lgi"]
    self.install_if = [self.parent, "lua5.1"]
    return ["usr/lib/libpeas-2/loaders/liblua51loader.so"]


@subpackage("libpeas2-gjs")
def _(self):
    self.subdesc = "GJS support"
    self.install_if = [self.parent, "gjs"]
    return ["usr/lib/libpeas-2/loaders/libgjsloader.so"]

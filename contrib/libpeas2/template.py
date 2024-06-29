pkgname = "libpeas2"
pkgver = "2.0.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dvapi=true"]
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
    "glib-devel",
    "gjs-devel",
    "gtk+3-devel",
    "lua5.1-devel",
    "python-devel",
    "python-gobject-devel",
]
checkdepends = ["xwayland-run", "fonts-dejavu-ttf"]
pkgdesc = "GObject application plugin library (2.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Libpeas"
source = f"$(GNOME_SITE)/libpeas/{pkgver[:-2]}/libpeas-{pkgver}.tar.xz"
sha256 = "39e3b507c29d2d01df1345e9b3380fd7a9d0aeb5b2e657d38e6c2bea5023e5f0"
# fails
options = ["!cross"]


@subpackage("libpeas2-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpeas2-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (python support)"
    self.depends += ["python-gobject"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "python"]
    return ["usr/lib/libpeas-2/loaders/libpythonloader.so"]


@subpackage("libpeas2-lua")
def _lua(self):
    self.pkgdesc = f"{pkgdesc} (lua 5.1 support)"
    self.depends += ["lua5.1-lgi"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "lua5.1"]
    return ["usr/lib/libpeas-2/loaders/liblua51loader.so"]


@subpackage("libpeas2-gjs")
def _gjs(self):
    self.pkgdesc = f"{pkgdesc} (gjs support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gjs"]
    return ["usr/lib/libpeas-2/loaders/libgjsloader.so"]

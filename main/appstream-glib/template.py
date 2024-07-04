pkgname = "appstream-glib"
pkgver = "0.8.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
    "-Dgtk-doc=false",
    "-Drpm=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "vala",
    "gobject-introspection",
    "libcurl-devel",
    "libyaml-devel",
    "gperf",
]
makedepends = [
    "glib-devel",
    "gcab-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libcurl-devel",
    "libyaml-devel",
]
pkgdesc = "AppStream metadata library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://people.freedesktop.org/~hughsient/appstream-glib"
source = f"https://people.freedesktop.org/~hughsient/{pkgname}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "84754064c560fca6e1ab151dc64354fc235a5798f016b91b38c9617253a8cf11"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/share/installed-tests")


@subpackage("appstream-glib-devel")
def _devel(self):
    return self.default_devel()

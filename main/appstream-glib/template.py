pkgname = "appstream-glib"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true", "-Dgtk-doc=false", "-Drpm=false", "-Dstemmer=false"
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "vala", "gobject-introspection",
    "libcurl-devel", "libyaml-devel", "gperf",
]
makedepends = [
    "glib-devel", "gcab-devel", "gtk+3-devel", "json-glib-devel",
    "libarchive-devel", "libcurl-devel", "libyaml-devel"
]
pkgdesc = "AppStream metadata library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://people.freedesktop.org/~hughsient/appstream-glib"
source = f"https://people.freedesktop.org/~hughsient/{pkgname}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "71256500add5048d6f08878904708b3d0c3875f402e0adcd358e91d47dcd8b96"
options = ["!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/share/installed-tests", recursive = True)

@subpackage("appstream-glib-devel")
def _devel(self):
    return self.default_devel()

pkgname = "uhttpmock"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "libsoup-devel",
]
pkgdesc = "HTTP service mocking library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/pwithnall/uhttpmock"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "881b17c23b1a20b8a05b3598af584e9d1e94a4902cc53920548dc16f24c884c7"
# gobject-introspection
options = ["!cross"]


@subpackage("uhttpmock-devel")
def _devel(self):
    return self.default_devel()

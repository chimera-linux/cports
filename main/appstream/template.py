pkgname = "appstream"
# match to contrib/appstream-qt
pkgver = "1.0.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dapidocs=false",
    "-Dcompose=true",
    "-Dstemming=false",
    "-Dsystemd=false",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "gobject-introspection",
    "gperf",
    "itstool",
    "meson",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "cairo-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libcurl-devel",
    "librsvg-devel",
    "libxml2-devel",
    "libxmlb-devel",
    "libyaml-devel",
    "pango-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Tools and libraries to work with AppStream metadata"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "http://www.freedesktop.org/wiki/Distributions/AppStream"
source = (
    f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "dd7222519b5d855124fa803ce82a7cbf090ac6b2e44a5bc515e729b1f20a63ae"
options = ["!cross"]


@subpackage("appstream-devel")
def _devel(self):
    return self.default_devel()

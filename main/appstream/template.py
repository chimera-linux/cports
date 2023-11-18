pkgname = "appstream"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false", "-Dstemming=false", "-Dapidocs=false"]
hostmakedepends = [
    "pkgconf",
    "meson",
    "gperf",
    "gettext",
    "itstool",
    "xsltproc",
    "gobject-introspection",
    "docbook-xsl-nons",
]
makedepends = [
    "glib-devel",
    "libxmlb-devel",
    "libxml2-devel",
    "libyaml-devel",
    "libcurl-devel",
]
pkgdesc = "Tools and libraries to work with AppStream metadata"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "http://www.freedesktop.org/wiki/Distributions/AppStream"
source = (
    f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e964fea8b4b7efac7976dc13da856421ddec4299acb5012a7c059f03eabcbeae"
options = ["!cross"]


@subpackage("appstream-devel")
def _devel(self):
    return self.default_devel()

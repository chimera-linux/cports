pkgname = "appstream"
pkgver = "1.0.1"
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
depends = ["shared-mime-info"]
pkgdesc = "Tools and libraries to work with AppStream metadata"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "http://www.freedesktop.org/wiki/Distributions/AppStream"
source = (
    f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3a6877c887627aed515e9802f63ac7bd83fffab4c2cad33c809c692c4bd8da48"
options = ["!cross"]


@subpackage("appstream-devel")
def _devel(self):
    return self.default_devel()

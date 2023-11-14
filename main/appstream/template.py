pkgname = "appstream"
pkgver = "0.16.4"
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
sha256 = "95d5cf451d1945182a9bc4d597c13e713451a3dba1a5759f45b6b3279ff3774c"
options = ["!cross"]


@subpackage("appstream-devel")
def _devel(self):
    return self.default_devel()

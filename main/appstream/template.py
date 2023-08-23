pkgname = "appstream"
pkgver = "0.16.3"
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
sha256 = "4470a27474dc3cc4938552fbf0394b6a65d8a2055d4f4418df086d65d8f2ba29"
options = ["!cross"]


@subpackage("appstream-devel")
def _devel(self):
    return self.default_devel()

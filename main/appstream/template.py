pkgname = "appstream"
pkgver = "1.0.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dapidocs=false",
    "-Dcompose=true",
    "-Dqt=true",
    "-Dqt-versions=6",
    "-Dstemming=false",
    "-Dsystemd=false",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "gobject-introspection",
    "gperf",
    "itstool",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "curl-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "librsvg-devel",
    "libxml2-devel",
    "libxmlb-devel",
    "libyaml-devel",
    "pango-devel",
    "qt6-qtbase-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Tools and libraries to work with AppStream metadata"
license = "LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Distributions/AppStream"
source = (
    f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3289568eeaaa84365dcfc8a6be2b547a9abe05cec6d3f08b62f39e832a6e7cb9"
# gir
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/share/installed-tests")


@subpackage("appstream-qt")
def _(self):
    self.subdesc = "Qt support"

    return [
        "usr/lib/libAppStreamQt.so.*",
    ]


@subpackage("appstream-qt-devel")
def _(self):
    self.depends = [self.with_pkgver("appstream-devel")]
    self.subdesc = "Qt development files"

    return [
        "usr/include/AppStreamQt",
        "usr/lib/libAppStreamQt.so",
        "usr/lib/cmake/AppStreamQt",
    ]


@subpackage("appstream-devel")
def _(self):
    return self.default_devel()

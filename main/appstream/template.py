pkgname = "appstream"
pkgver = "1.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dapidocs=false",
    "-Dcompose=true",
    "-Dqt=true",
    "-Dstemming=false",
    "-Dsystemd=true",
]
hostmakedepends = [
    "bash-completion",
    "docbook-xsl",
    "gettext",
    "gobject-introspection",
    "gperf",
    "itstool",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "blake3-devel",
    "cairo-devel",
    "curl-devel",
    "elogind-devel",
    "fontconfig-devel",
    "freetype-devel",
    "glib-devel",
    "libfyaml-devel",
    "libvips-devel",
    "libxml2-devel",
    "libxmlb-devel",
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
sha256 = "2bc53d1d63ae28e7409a15747d4ae23a557409249461aab87a7947640402d1bd"
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

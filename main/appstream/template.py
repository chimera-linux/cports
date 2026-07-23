pkgname = "appstream"
pkgver = "1.1.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dapidocs=false",
    "-Dcompose=true",
    "-Dqt=true",
    "-Dstemming=false",
    "-Dsystemd=false",
]
# exclude as-test_yaml - fails with latest libfyaml even:
# https://github.com/ximion/appstream/issues/756
make_check_args = [
    "AppStream:as-validate_metainfo.cli",
    "AppStream:as-validate_metainfo.compose",
    "AppStream:as-test_basic",
    "AppStream:as-test_xml",
    "AppStream:as-test_validate",
    "AppStream:as-test_perf",
    "AppStream:as-test_misc",
    "AppStream:as-test_qt-misc",
    "AppStream:as-test_qt-pool",
    "AppStream:as-test_compose",
    "AppStream:as-test_pool",
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
    "fontconfig-devel",
    "freetype-devel",
    "glib-devel",
    "libfyaml-devel",
    "librsvg-devel",
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
sha256 = "0cba35762201ab9e367d5b8da4d0a6c3bd456103ac78b852585995318d6f109a"
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

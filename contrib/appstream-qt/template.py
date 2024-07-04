pkgname = "appstream-qt"
# match to main/appstream
pkgver = "1.0.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dapidocs=false",
    "-Dstemming=false",
    "-Dqt=true",
    "-Dqt-versions=6",
    "-Dgir=false",
    "-Dsvg-support=false",
    "-Dinstall-docs=false",
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
    "appstream-devel",
    "glib-devel",
    "libcurl-devel",
    "libxml2-devel",
    "libxmlb-devel",
    "libyaml-devel",
    "qt6-qtbase-devel",
]
origin = "appstream"
pkgdesc = "Tools and libraries to work with AppStream metadata (Qt library)"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "http://www.freedesktop.org/wiki/Distributions/AppStream"
source = (
    f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "dd7222519b5d855124fa803ce82a7cbf090ac6b2e44a5bc515e729b1f20a63ae"
options = ["!cross"]


def post_install(self):
    # appstream-qt is only these:
    # keep = [
    #     "usr/include/AppStreamQt",
    #     "usr/lib/cmake",
    #     "usr/lib/libAppStreamQt*",
    # ]
    self.uninstall("usr/bin")
    self.uninstall("usr/include/appstream")
    self.uninstall("usr/lib/libappstream.*", glob=True)
    self.uninstall("usr/lib/pkgconfig")
    self.uninstall("usr/share")


@subpackage("appstream-qt-devel")
def _devel(self):
    self.depends += ["appstream-devel"]
    return self.default_devel()

pkgname = "appstream-glib"
pkgver = "0.8.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
    "-Dgtk-doc=false",
    "-Drpm=false",
]
hostmakedepends = [
    "curl-devel",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "libyaml-devel",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "curl-devel",
    "gcab-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libyaml-devel",
]
pkgdesc = "AppStream metadata library"
license = "LGPL-2.1-or-later"
url = "https://people.freedesktop.org/~hughsient/appstream-glib"
source = f"https://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-{pkgver}.tar.xz"
sha256 = "132575f3ef2712cd0fc8a7f0c9287ff5c4264d75921953220dd2089911272946"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/share/installed-tests")


@subpackage("appstream-glib-devel")
def _(self):
    return self.default_devel()

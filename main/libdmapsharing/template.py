pkgname = "libdmapsharing"
pkgver = "3.9.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-tests"]
make_dir = "."
hostmakedepends = [
    "automake",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "avahi-glib-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "libgee-devel",
    "libsoup-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["check-devel"]
pkgdesc = "Library implementing the DMAP family of protocols"
license = "LGPL-2.1-or-later"
url = "https://www.flyn.org/projects/libdmapsharing/index.html"
source = f"https://www.flyn.org/projects/libdmapsharing/libdmapsharing-{pkgver}.tar.gz"
sha256 = "3659f63f29e11d6d6ae78b53d7cc6be3f3adeff9c00c67cc50ad19c6af699f7a"
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# FIXME: two tests fail
options = ["!check", "!cross"]
# FIXME: Otherwise tests fail with


@subpackage("libdmapsharing-devel")
def _(self):
    return self.default_devel()

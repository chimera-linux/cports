pkgname = "libdmapsharing"
pkgver = "3.9.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-tests"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
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
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://www.flyn.org/projects/libdmapsharing/index.html"
source = f"https://www.flyn.org/projects/libdmapsharing/libdmapsharing-{pkgver}.tar.gz"
sha256 = "3659f63f29e11d6d6ae78b53d7cc6be3f3adeff9c00c67cc50ad19c6af699f7a"
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# FIXME: two tests fail
options = ["!check", "!cross"]
# FIXME: Otherwise tests fail with
# make[4]: argument 'observer-auth=fifo:/tmp/GMfifo2' to option '-j' must be a positive number
exec_wrappers = [("/usr/bin/gmake", "make")]


@subpackage("libdmapsharing-devel")
def _devel(self):
    return self.default_devel()

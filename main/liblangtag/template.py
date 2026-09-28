pkgname = "liblangtag"
pkgver = "0.6.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gobject-introspection",
    "gsed",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["glib-devel", "libxml2-devel"]
pkgdesc = "Interface library to access tags for identifying languages"
license = "MPL-2.0 OR LGPL-3.0-or-later"
url = "https://gitlab.com/tagoh/liblangtag"
source = f"{url}/-/releases/{pkgver}/downloads/liblangtag-{pkgver}.tar.gz"
sha256 = "f98d15a2039a523e6ad7796bba0fb003f214db57cc4ad2e12e2f8ab12d309694"
# bunch of nonportable fuckery
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("liblangtag-devel")
def _(self):
    return self.default_devel()

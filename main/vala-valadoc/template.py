pkgname = "vala-valadoc"
pkgver = "0.56.19"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xml",
    "flex",
    "libtool",
    "libxslt-progs",
    "pkgconf",
]
makedepends = [
    "flex-devel-static",
    "glib-devel",
    "gobject-introspection-devel",
    "graphviz-devel",
    "vala-devel",
]
checkdepends = ["dbus", "gobject-introspection-devel", "bash"]
pkgdesc = "Vala documentation tool"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Vala"
source = (
    f"$(GNOME_SITE)/vala/{pkgver[0 : pkgver.rfind('.')]}/vala-{pkgver}.tar.xz"
)
sha256 = "5ad7cbbfcc0de61b403d6797c9ef60455bfbebd8e162aec33b5b0b097adfb9d5"
# don't duplicate the test run
options = ["!check"]


def install(self):
    self.make.install(wrksrc=f"{self.make_dir}/libvaladoc")
    self.make.install(wrksrc=f"{self.make_dir}/valadoc")
    self.install_man("doc/valadoc.1")


@subpackage("vala-valadoc-libs")
def _(self):
    self.pkgdesc = "Vala documentation tool"
    self.renames = ["libvaladoc"]

    return self.default_libs(extra=["usr/lib/valadoc-*", "usr/share/valadoc-*"])


@subpackage("vala-valadoc-devel")
def _(self):
    self.renames = ["valadoc-devel"]

    return self.default_devel()

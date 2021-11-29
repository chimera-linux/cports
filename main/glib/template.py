pkgname = "glib"
_mver = "2.70"
pkgver = f"{_mver}.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dfam=false", "-Dman=true", "-Dgtk_doc=true", "-Dselinux=disabled",
]
hostmakedepends = [
    "meson", "gettext-tiny", "pkgconf", "docbook-xsl-nons", "xsltproc",
    "gtk-doc"
]
makedepends = [
    "zlib-devel", "pcre-devel", "libffi-devel", "dbus-devel",
    "elftoolchain-devel", "libmount-devel",
]
# not yet all available
checkdepends = [
    "desktop-file-utils", "shared-mime-info", "dbus", "python-pytest"
]
triggers = ["/usr/share/glib-2.0/schemas"]
pkgdesc = "GLib library of C routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/{pkgname}/{_mver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f9b7bce7f51753a1f43853bbcaca8bf09e15e994268e29cfd7a76f65636263c0"
# missing checkdepends
options = ["!check"]

def do_check(self):
    self.do("dbus-run-session", "ninja", "-C", "build", "test")

def post_install(self):
    self.install_license("COPYING")

@subpackage("libglib-static")
def _static(self):
    self.pkgdesc = f"{pkgdesc} (static libraries)"

    return self.default_static()

@subpackage("libglib-devel")
def _libdevel(self):
    self.pkgdesc = f"{pkgdesc} (library development files)"

    return [
        "usr/include",
        "usr/lib/glib-2.0",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
    ]

@subpackage("glib-devel")
def _devel(self):
    self.depends += [f"libglib-devel={pkgver}-r{pkgrel}"]
    self.pycompile_dirs = [
        "usr/share/glib-2.0/codegen", "usr/share/glib-2.0/gdb"
    ]

    return self.default_devel(extra = [
        "usr/bin/glib-compile-resources",
        "usr/bin/glib-genmarshal",
        "usr/bin/glib-gettextize",
        "usr/bin/glib-mkenums",
        "usr/bin/gtester",
        "usr/bin/gtester-report",
        "usr/bin/gdbus-codegen",
        "usr/share/man/man1/glib-compile-resources.1",
        "usr/share/man/man1/glib-genmarshal.1",
        "usr/share/man/man1/glib-gettextize.1",
        "usr/share/man/man1/glib-mkenums.1",
        "usr/share/man/man1/gtester.1",
        "usr/share/man/man1/gtester-report.1",
        "usr/share/man/man1/gdbus-codegen.1",
        "usr/share/glib-2.0",
        "usr/share/gdb",
    ])

@subpackage("glib-doc")
def _doc(self):
    return self.default_doc()

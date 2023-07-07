pkgname = "glib"
pkgver = "2.76.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtk_doc=false",
    "-Dman=true",
    "-Dselinux=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "gettext-tiny",
    "pkgconf",
    "docbook-xsl-nons",
    "xsltproc",
]
makedepends = [
    "zlib-devel",
    "pcre2-devel",
    "libffi-devel",
    "dbus-devel",
    "elftoolchain-devel",
    "libmount-devel",
]
checkdepends = [
    "desktop-file-utils",
    "shared-mime-info",
    "dbus",
    "python-pytest",
]
triggers = ["/usr/share/glib-2.0/schemas", "/usr/lib/gio/modules"]
pkgdesc = "GLib library of C routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5a5a191c96836e166a7771f7ea6ca2b0069c603c7da3cba1cd38d1694a395dda"
# FIXME int - e.g. g_ascii_strtoll fails
hardening = ["!int"]
# cyclic with desktop-file-utils
options = ["!check"]


def post_install(self):
    from cbuild.util import python

    self.install_license("COPYING")

    python.precompile(self, "usr/share/glib-2.0/codegen")
    python.precompile(self, "usr/share/glib-2.0/gdb")


@subpackage("glib-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/bin/glib-compile-resources",
            "usr/bin/glib-genmarshal",
            "usr/bin/glib-gettextize",
            "usr/bin/glib-mkenums",
            "usr/bin/gtester",
            "usr/bin/gtester-report",
            "usr/bin/gdbus-codegen",
            "usr/lib/glib-2.0",
            "usr/share/man/man1/glib-compile-resources.1",
            "usr/share/man/man1/glib-genmarshal.1",
            "usr/share/man/man1/glib-gettextize.1",
            "usr/share/man/man1/glib-mkenums.1",
            "usr/share/man/man1/gtester.1",
            "usr/share/man/man1/gtester-report.1",
            "usr/share/man/man1/gdbus-codegen.1",
            "usr/share/glib-2.0",
            "usr/share/gdb",
        ]
    )

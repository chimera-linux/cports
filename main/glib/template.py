pkgname = "glib"
pkgver = "2.82.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false",
    "-Dintrospection=enabled",
    "-Dman-pages=enabled",
    "-Dselinux=disabled",
]
make_check_args = ["--timeout-multiplier", "5"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-docutils",
    "python-packaging",
]
makedepends = [
    "dbus-devel",
    "elfutils-devel",
    "freetype-bootstrap",
    "glib-bootstrap",
    "libffi-devel",
    "libmount-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
checkdepends = [
    "dbus",
    "python-pytest",
]
# introspection data now lives here
replaces = ["gir-freedesktop<1.80.0"]
triggers = ["/usr/share/glib-2.0/schemas", "/usr/lib/gio/modules"]
pkgdesc = "GLib library of C routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/glib/{pkgver[:-2]}/glib-{pkgver}.tar.xz"
sha256 = "478634440bf52ee4ec4428d558787398c0be6b043c521beb308334b3db4489a6"
# FIXME int - strfuncs failure
hardening = ["!int"]


if self.profile().arch == "riscv64":
    # ftbfs
    configure_args += ["-Dtests=false"]


def post_install(self):
    from cbuild.util import python

    self.install_license("COPYING")

    python.precompile(self, "usr/share/glib-2.0/codegen")
    python.precompile(self, "usr/share/glib-2.0/gdb")


@subpackage("glib-devel")
def _(self):
    self.depends += ["python-packaging"]
    self.replaces = ["libgirepository-devel<1.80"]
    self.provider_priority = 100
    return self.default_devel(
        extra=[
            "cmd:glib-compile-resources",
            "cmd:glib-genmarshal",
            "cmd:glib-gettextize",
            "cmd:glib-mkenums",
            "cmd:gtester",
            "cmd:gtester-report",
            "cmd:gdbus-codegen",
            "usr/lib/glib-2.0",
            "usr/share/glib-2.0",
            "usr/share/gdb",
        ]
    )

pkgname = "glib"
pkgver = "2.82.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false",
    "-Dintrospection=enabled",
    "-Dman-pages=enabled",
    "-Dselinux=disabled",
    "-Dsysprof=enabled",
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
    "libffi8-devel",
    "pcre2-devel",
    "sysprof-capture",
    "util-linux-mount-devel",
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
sha256 = "37dd0877fe964cd15e9a2710b044a1830fb1bd93652a6d0cb6b8b2dff187c709"
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

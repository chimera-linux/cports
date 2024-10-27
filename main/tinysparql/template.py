pkgname = "tinysparql"
pkgver = "3.8.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "asciidoc",
    "xsltproc",
    "dbus",
    "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "icu-devel",
    "json-glib-devel",
    "libxml2-devel",
    "sqlite-devel",
    "libsoup-devel",
    "bash-completion",
]
depends = ["shared-mime-info"]
checkdepends = ["mandoc"]
provides = [self.with_pkgver("tracker")]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/tinysparql/{pkgver[:-2]}/tinysparql-{pkgver}.tar.xz"
sha256 = "c0fcda77520f531548b2395137dcd193ee9cde5e222d3c9d273f030d1762a504"
# check may be disabled
options = ["!cross"]


if self.profile().arch == "ppc64le":
    # https://gitlab.gnome.org/GNOME/tinysparql/-/issues/474
    options += ["!check"]


@subpackage("tinysparql-devel")
def _(self):
    self.provides = [self.with_pkgver("tracker-devel")]
    return self.default_devel()


@subpackage("tinysparql-libs")
def _(self):
    self.provides = [self.with_pkgver("tracker-libs")]
    return self.default_libs()

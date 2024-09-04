pkgname = "tinysparql"
pkgver = "3.8_rc"
pkgrel = 0
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
# transitional
provides = [self.with_pkgver("tracker")]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/tinysparql/{pkgver[:3]}/tinysparql-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "a86aa73a72f56d81f4b9f0eec6aefbc45ab35f9a8433c47722d8380b6637c475"
# check FIXME: __main__.TestCli.test_help fails with no error
options = ["!cross", "!check"]


@subpackage("tinysparql-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("tracker-devel")]
    return self.default_devel()


@subpackage("tinysparql-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("tracker-libs")]
    return self.default_libs()

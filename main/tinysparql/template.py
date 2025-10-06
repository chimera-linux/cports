pkgname = "tinysparql"
pkgver = "3.10.0"
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
    "asciidoc",
    "dbus",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "python-gobject",
    "vala",
]
makedepends = [
    "bash-completion",
    "dbus-devel",
    "glib-devel",
    "icu-devel",
    "json-glib-devel",
    "libsoup-devel",
    "libxml2-devel",
    "sqlite-devel",
]
depends = ["shared-mime-info"]
checkdepends = ["mandoc"]
renames = ["tracker"]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tinysparql"
source = f"$(GNOME_SITE)/tinysparql/{pkgver[:-2]}/tinysparql-{pkgver}.tar.xz"
sha256 = "fb0af98355ea1db700764cf4fa245884a199ca145ed42ed55f9a18c68552ca30"
options = ["!cross"]


@subpackage("tinysparql-devel")
def _(self):
    self.renames = ["tracker-devel"]
    return self.default_devel()


@subpackage("tinysparql-libs")
def _(self):
    self.renames = ["tracker-libs"]
    return self.default_libs()

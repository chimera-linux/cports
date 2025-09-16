pkgname = "colord"
pkgver = "1.4.8"
pkgrel = 0
build_style = "meson"
# manpages fail to generate
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddaemon_user=_colord",
    "-Dsystemd=false",
    "-Dargyllcms_sensor=false",
    "-Ddocs=false",
    "-Dman=false",
    "-Dsane=true",
    "-Dvapi=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "bash-completion",
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "lcms2-devel",
    "libgudev-devel",
    "libgusb-devel",
    "polkit-devel",
    "sane-backends-devel",
    "sqlite-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Color management daemon"
license = "GPL-2.0-only"
url = "https://www.freedesktop.org/software/colord"
source = f"{url}/releases/colord-{pkgver}.tar.xz"
sha256 = "21500bd68975312a7f0f3ce6019d9f75f42aacaa75ca7115ec720b5445406896"
# FIXME int
hardening = ["!int"]

if self.profile().cross:
    hostmakedepends.append("colord")


def post_install(self):
    self.install_service("^/colord")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")


@subpackage("colord-libs")
def _(self):
    self.renames = ["libcolord"]

    return self.default_libs()


@subpackage("colord-devel")
def _(self):
    return self.default_devel()

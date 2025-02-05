pkgname = "colord"
pkgver = "1.4.7"
pkgrel = 4
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
    "lcms2-devel",
    "libgudev-devel",
    "libgusb-devel",
    "polkit-devel",
    "sane-backends-devel",
    "sqlite-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Color management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.freedesktop.org/software/colord"
source = f"{url}/releases/colord-{pkgver}.tar.xz"
sha256 = "de02d9910634ae159547585cec414e450f711c27235453b4f9b38a9f2361a653"
# FIXME int
hardening = ["!int"]

if self.profile().cross:
    hostmakedepends.append("colord")


def post_install(self):
    self.install_service(self.files_path / "colord")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("colord-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libcolord")]

    return self.default_libs()


@subpackage("colord-devel")
def _(self):
    return self.default_devel()

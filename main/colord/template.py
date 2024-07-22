pkgname = "colord"
pkgver = "1.4.7"
pkgrel = 1
build_style = "meson"
# manpages fail to generate
configure_args = [
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


@subpackage("libcolord")
def _lib(self):
    self.subdesc = "shared library"

    return self.default_libs()


@subpackage("colord-devel")
def _devel(self):
    return self.default_devel()

pkgname = "colord"
pkgver = "1.4.6"
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
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "vala",
]
makedepends = [
    "bash-completion",
    "lcms2-devel",
    "libgudev-devel",
    "libgusb-devel",
    "polkit-devel",
    "sqlite-devel",
    "dbus-devel",
    "sane-backends-devel",
]
pkgdesc = "Color management daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.freedesktop.org/software/colord"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "7407631a27bfe5d1b672e7ae42777001c105d860b7b7392283c8c6300de88e6f"
# FIXME int
hardening = ["!int"]
# assertion failed (cd_edid_get_vendor_name (edid) == "LG"): (NULL == "LG")
options = ["!check"]

if self.profile().cross:
    hostmakedepends.append("colord")


def post_install(self):
    self.install_service(self.files_path / "colord")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="colord.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="colord.conf",
    )


@subpackage("libcolord")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (shared library)"

    return self.default_libs()


@subpackage("colord-devel")
def _devel(self):
    return self.default_devel()

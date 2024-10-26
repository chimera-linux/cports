pkgname = "thermald"
pkgver = "2.5.8"
pkgrel = 2
archs = ["x86_64"]
# don't use autogen.sh, it generates files that force reconf in build phase
build_style = "gnu_configure"
configure_args = ["--with-dbus-power-group=_thermald"]
make_dir = "."
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gettext",
    "glib-devel",
    "gtk-doc-tools",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libevdev-devel",
    "libxml2-devel",
    "upower-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Thermal daemon for x86_64-based Intel CPUs"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/thermal_daemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "365fbb91d5b986ecbac7fe70d6993bc5a4d47e07dfca9d832204fe8ec0a7094b"
hardening = ["vis", "!cfi"]


# autoreconf fails otherwise
def pre_configure(self):
    self.mkdir("m4")


def post_install(self):
    self.install_file(
        "data/org.freedesktop.thermald.service.in",
        "usr/share/dbus-1/system-services",
        0o644,
        "org.freedesktop.thermald.service",
    )
    self.install_license("COPYING")
    self.install_service(self.files_path / "thermald")
    self.install_sysusers(self.files_path / "sysusers.conf")

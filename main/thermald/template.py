pkgname = "thermald"
pkgver = "2.5.12"
pkgrel = 0
archs = ["x86_64"]
# don't use autogen.sh, it generates files that force reconf in build phase
build_style = "gnu_configure"
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
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "libevdev-devel",
    "libxml2-devel",
    "upower-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Thermal daemon for x86_64-based Intel CPUs"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/thermal_daemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f0698f8295b1c4f57673462e7c3a970d0fc328d56d80c0b9ab35644f5dbb72a9"
hardening = ["vis", "!cfi"]
options = ["etcfiles"]


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

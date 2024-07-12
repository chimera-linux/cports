pkgname = "thermald"
pkgver = "2.5.7"
pkgrel = 1
archs = ["x86_64"]
# don't use autogen.sh, it generates files that force reconf in do_build
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gettext",
    "glib-devel",
    "gmake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libevdev-devel",
    "libxml2-devel",
    "upower-devel",
]
pkgdesc = "Thermal daemon for x86_64-based Intel CPUs"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/thermal_daemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b7df06bbd813bf039893a533d1e30073102a2494f6fdd432ae7c05f376c7cc15"
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

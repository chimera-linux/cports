pkgname = "thermald"
pkgver = "2.5.6"
pkgrel = 0
archs = ["x86_64"]
# don't use autogen.sh, it generates files that force reconf in do_build
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "dbus-glib",
    "gettext",
    "glib-devel",
    "gmake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "dbus-glib-devel",
    "glib-devel",
    "libevdev-devel",
    "libxml2-devel",
    "upower-devel",
    "xz-devel",
]
pkgdesc = "Thermal daemon for x86_64-based Intel CPUs"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/thermal_daemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e5a452624f133d71f4aff0bd0c8f8258399a5ae1a7d5aea177fa6a6e33dad1fd"
# TODO: cfi
hardening = ["vis"]


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

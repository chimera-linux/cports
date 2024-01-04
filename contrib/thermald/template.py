pkgname = "thermald"
pkgver = "2.5.4"
pkgrel = 0
archs = ["x86_64"]
build_style = "gnu_configure"
# TODO: figure out why we need to disable dependency tracking
configure_args = ["--disable-dependency-tracking"]
configure_env = {"NO_CONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "autoconf",
    "autoconf-archive",
    "automake",
    "gettext",
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
sha256 = "2addedfc7974b30ed6a553a5690961eb48d6abacd4584e3b6d3fd292343d694e"
hardening = ["vis"]


def post_install(self):
    self.install_file(
        "data/org.freedesktop.thermald.service.in",
        "usr/share/dbus-1/system-services",
        0o644,
        "org.freedesktop.thermald.service",
    )
    self.install_license("COPYING")
    self.install_service(self.files_path / "thermald")

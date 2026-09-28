pkgname = "intel-lpmd"
pkgver = "0.1.0"
pkgrel = 0
archs = ["x86_64"]
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
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
    "elogind-devel",
    "glib-devel",
    "libnl-devel",
    "libxml2-devel",
    "linux-headers",
    "upower-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Intel Low Power Mode Daemon"
license = "GPL-2.0-or-later"
url = "https://github.com/intel/intel-lpmd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e5de3dd4ec9496430b3e3c31e69830cc8e974f7a0d0e8bf4e3c1d5cf5834f8ed"


def post_install(self):
    self.rename("etc/dbus-1", "usr/share/dbus-1", relative=False)
    self.rename("etc/intel_lpmd", "usr/share/intel_lpmd", relative=False)
    self.install_service(self.files_path / "intel-lpmd")

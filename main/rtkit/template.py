pkgname = "rtkit"
pkgver = "0.14"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibsystemd=disabled",
    "-Dinstalled_tests=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "libcap-devel",
    "polkit-devel",
    "zlib-ng-compat-devel",
]
depends = ["dinit-dbus", "polkit"]
pkgdesc = "Realtime policy and watchdog daemon"
license = "MIT AND GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/pipewire/rtkit"
source = f"{url}/-/archive/v{pkgver}/rtkit-v{pkgver}.tar.gz"
sha256 = "55dd379b11f52b81655e2dc676de9d602d050cb0beb18ef01f0f65569f0a5e59"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs to be regenerated on every release
    self.cp(self.files_path / "xml-introspection.h", ".")


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "rtkit")
    # upstream uses different full name and home directory
    self.uninstall("usr/lib/sysusers.d/rtkit.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    # optional
    self.install_file(
        self.files_path / "50-rtkit.rules", "usr/share/polkit-1/rules.d"
    )

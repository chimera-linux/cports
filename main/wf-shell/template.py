pkgname = "wf-shell"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "alsa-lib-devel",
    "ddcutil-devel",
    "gtk4-layer-shell-devel",
    "gtkmm-devel",
    "libdbusmenu-devel",
    "libpulse-devel",
    "linux-pam-devel",
    "openssl3-devel",
    "pipewire-devel",
    "wayfire-devel",
    "wayland-protocols",
    "wireplumber-devel",
    "yyjson-devel",
]
pkgdesc = "Desktop shell for Wayfire"
license = "MIT"
url = "https://wayfire.org"
_wfjson = "a85b53d8a45565b876465bdf7482776eb01cc54a"
_wlogout = "1cffc6fd0be5d8127f394b25eb3c82e71fbaabe1"
_gvc = "5f9768a2eac29c1ed56f1fbb449a77a3523683b6"
source = [
    f"https://github.com/WayfireWM/wf-shell/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/WayfireWM/wf-json/archive/{_wfjson}.tar.gz",
    f"https://github.com/soreau/wayland-logout/archive/{_wlogout}.tar.gz",
    f"https://github.com/GNOME/libgnome-volume-control/archive/{_gvc}.tar.gz",
]
source_paths = [
    ".",
    "subprojects/wf-json",
    "subprojects/wayland-logout",
    "subprojects/gvc",
]
sha256 = [
    "328b1a01c5fc63ebc6fa79152bafdcd2e1525c8bb3caf5b49361ff2792dd57f4",
    "91cec007677cbf83e84aae0abd0cc4436dbef142fd9bede01b6df289b4df3e06",
    "1999dcab22ccf159b56e670476c0f6eab309ac2f69d16ad3c117824f17201313",
    "0163f8e7250d46a18905b04e966f3a4c849a3afb810ca1e862cb685f8a92bc2e",
]

options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    (self.destdir / "usr/lib/pam.d").mkdir(parents=True, exist_ok=True)
    (self.destdir / "etc/pam.d/wf-locker").rename(
        self.destdir / "usr/lib/pam.d/wf-locker"
    )
    (self.destdir / "etc/pam.d").rmdir()

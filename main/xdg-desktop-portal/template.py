pkgname = "xdg-desktop-portal"
pkgver = "1.20.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bubblewrap",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "flatpak-devel",
    "fuse-devel",
    "gdk-pixbuf-devel",
    "geoclue-devel",
    "gst-plugins-base-devel",
    "json-glib-devel",
    "libportal-devel",
    "pipewire-devel",
]
checkdepends = [
    "bash",
    "dbus",
    "gstreamer",
    "gst-plugins-good",
    "python-dbus",
    "python-dbusmock",
    "python-gobject",
    "python-pytest",
    "umockdev-devel",
]
pkgdesc = "Desktop integration portal"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal"
source = f"https://github.com/flatpak/xdg-desktop-portal/releases/download/{pkgver}/xdg-desktop-portal-{pkgver}.tar.xz"
sha256 = "33d666f169efdf3f3bedd531bdbd272edc8f471caf6ca6cf6752efbbab57523a"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()

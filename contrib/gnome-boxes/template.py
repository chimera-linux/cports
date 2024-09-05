pkgname = "gnome-boxes"
pkgver = "47_beta"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "libarchive-devel",
    "libhandy-devel",
    "libosinfo-devel",
    "libportal-devel",
    "libsoup-devel",
    "libusb-devel",
    "libvirt-glib-devel",
    "libxml2-devel",
    "spice-gtk-devel",
    "webkitgtk-devel",
]
depends = [
    "libvirt",
    "qemu",
]
pkgdesc = "QEMU frontend for GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://apps.gnome.org/Boxes"
source = f"$(GNOME_SITE)/gnome-boxes/{pkgver[:2]}/gnome-boxes-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "b6b9a60a90920f1889a7538727a0473335865917e53e42daf47876e5346d77be"
# gobject-introspection
# FIXME: lto makes the os-downloader crash (pick any os and it aborts instantly in os-downloader.vala)
options = ["!cross", "!lto"]

_arch = self.profile().arch
match _arch:
    case "x86_64" | "aarch64" | "riscv64":
        depends += [f"qemu-system-{_arch}"]
    case "ppc64le" | "ppc64":
        depends += ["qemu-system-ppc64"]

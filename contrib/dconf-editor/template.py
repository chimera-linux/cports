pkgname = "dconf-editor"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "dconf-devel",
    "gettext",
    "glib-devel",
    "libhandy-devel",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "dconf-devel",
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
]
pkgdesc = "Viewer and editor of applications internal dconf settings"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/dconf-editor"
source = f"$(GNOME_SITE)/dconf-editor/{pkgver[:-pkgver.rfind('.')]}/dconf-editor-{pkgver}.tar.xz"
sha256 = "935a3c2dd76cc2a93cd5aee9a54d3947fb111eb396f4b63dc5f0ba8f8d099136"

# vala broken
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}

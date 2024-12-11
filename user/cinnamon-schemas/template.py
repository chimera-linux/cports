pkgname = "cinnamon-schemas"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
# We only need the schemas, so disable features when possible
configure_args = [
    "-Dbuild_recorder=false",
    "-Ddisable_networkmanager=true",
    "-Dwayland=false",
]
hostmakedepends = [
    "bash",
    "gobject-introspection",
    "intltool",
    "libsass-python",
    "meson",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cinnamon-menus-devel",
    "cjs-devel",
    "dbus-devel",
    "gcr3-devel",
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxml2-devel",
    "mesa-devel",
    "muffin-devel",
    "polkit-devel",
    "xapp-devel",
]
pkgdesc = "Linux desktop that provides a traditional user experience"
subdesc = "schemas"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = (
    f"https://github.com/linuxmint/cinnamon/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "d668b7cf31b1a8719e8ff2831b8ca3209b5f5b8dd4380396217d43b7d8a21c63"
# meson.build: tests are not currently functional
options = ["!check", "!cross"]


def post_install(self):
    for directory in ["etc", "usr/bin", "usr/lib", "usr/libexec"]:
        self.uninstall(directory)

    for share_directory in [
        "applications",
        "cinnamon",
        "cinnamon-session",
        "dbus-1",
        "desktop-directories",
        "icons",
        "man",
        "polkit-1",
        "xdg-desktop-portal",
        "xsessions",
    ]:
        self.uninstall(f"usr/share/{share_directory}")

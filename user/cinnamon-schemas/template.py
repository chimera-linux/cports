pkgname = "cinnamon-schemas"
pkgver = "6.2.9"
pkgrel = 0
build_style = "meson"
# We only need the schemas, so disable features when possible
configure_args = ["-Dbuild_recorder=false", "-Ddisable_networkmanager=true"]
hostmakedepends = [
    "gobject-introspection",
    "intltool",
    "meson",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cinnamon-menus-devel",
    "cjs-devel",
    "dbus-devel",
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
sha256 = "a0b15b98a899532d531689ea11ff6805a87fcf5994e238322b6c916bf8c29919"
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
        "wayland-sessions",
        "xdg-desktop-portal",
        "xsessions",
    ]:
        self.uninstall(f"usr/share/{share_directory}")

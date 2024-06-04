pkgname = "snapshot"
pkgver = "46.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream",
    "cargo",
    "desktop-file-utils",
    "gettext",
    "gtk-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gstreamer-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "libadwaita-devel",
]
depends = [
    "gstreamer-libcamera",
    "gstreamer-pipewire",
]
pkgdesc = "GNOME camera app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Snapshot"
source = f"$(GNOME_SITE)/snapshot/{pkgver[:-2]}/snapshot-{pkgver}.tar.xz"
sha256 = "45957a0415f454d63531491aa04795cee0ced4edddd5d8fa0d000f5ef0735b67"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/snapshot")

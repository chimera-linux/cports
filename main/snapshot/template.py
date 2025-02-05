pkgname = "snapshot"
pkgver = "47.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libadwaita-devel",
    "libseccomp-devel",
    "rust-std",
]
depends = [
    "glycin-loaders",
    "gst-plugins-rs-gtk4",
    "gstreamer-libcamera",
    "gstreamer-pipewire",
]
pkgdesc = "GNOME camera app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Snapshot"
source = (
    f"$(GNOME_SITE)/snapshot/{pkgver.split('.')[0]}/snapshot-{pkgver}.tar.xz"
)
sha256 = "e4b162679af24c7e96ee6e22b47d5ff0da96e0a0f616d13aeb1207c609f89483"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/snapshot")

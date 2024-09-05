pkgname = "snapshot"
pkgver = "47_beta"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
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
    "gstreamer-libcamera",
    "gstreamer-pipewire",
]
# FIXME: drop clippy, required by "Cargo clippy - aperture" test which fails otherwise
checkdepends = ["rust-clippy"]
pkgdesc = "GNOME camera app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Snapshot"
source = f"$(GNOME_SITE)/snapshot/{pkgver[:2]}/snapshot-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "d06c673457acd61b928b8a4f64a0bb4b9f3b42b4c03ae39e8737768d93d146bc"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/snapshot")

pkgname = "snapshot"
pkgver = "48.0.1"
pkgrel = 1
build_style = "meson"
make_check_args = ["--timeout-multiplier=5"]
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
    "gst-plugins-bad",
    "gst-plugins-good",
    "gst-plugins-rs-gtk4",
    "libcamera-gstreamer",
    "pipewire-gstreamer",
]
pkgdesc = "GNOME camera app"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Snapshot"
source = (
    f"$(GNOME_SITE)/snapshot/{pkgver.split('.')[0]}/snapshot-{pkgver}.tar.xz"
)
sha256 = "393176859a20b7d235dfc303031ba20c686441106988dc911dd91b7b6d66e1fd"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/snapshot")

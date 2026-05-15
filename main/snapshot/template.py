pkgname = "snapshot"
pkgver = "50.0"
pkgrel = 0
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
    "glycin-gtk4-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "lcms2-devel",
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
sha256 = "ec9daf9883eb90330911bb51e6b69eed8c9dbdd5438e864adc90ee55a5fe9eed"


def post_extract(self):
    # we'll be re-vendoring all sources
    self.rm(".cargo/config.toml")


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/snapshot")

pkgname = "snapshot"
pkgver = "51.0"
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
sha256 = "3e64fa4cd1a742ae34b6f6d8e6d9614a2d3eab88a1b0071c11ab53617eb214c2"


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
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "snapshot"))

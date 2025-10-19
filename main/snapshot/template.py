pkgname = "snapshot"
pkgver = "49.0"
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
sha256 = "5f96193d2919c7355745d26a1b01f23c3cb30a93c742d583ec42927c4a45ae18"


def post_extract(self):
    # we'll be re-vendoring all sources
    self.rm(".cargo/config.toml")


def prepare(self):
    from cbuild.util import cargo

    # 0.2.175 is broken with rustix 1.0.8 on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.174",
        allow_network=True,
    )

    cargo.Cargo(self).vendor(wrksrc=".")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/snapshot")

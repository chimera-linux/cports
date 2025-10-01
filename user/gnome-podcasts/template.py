pkgname = "gnome-podcasts"
pkgver = "25.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "gst-plugins-bad-devel",
    "gstreamer-devel",
    "libadwaita-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "GTK-based podcast aggregator"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/podcasts"
source = f"{url}/-/archive/{pkgver}/podcasts-{pkgver}.tar.gz"
sha256 = "fb3f79cf4c5870d3debcbdf5a55e9f47ac22c1078cfcb76740262dfe77800949"
# check: broken tests due to sandboxing
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"build/podcasts-gtk/src/{self.profile().triplet}/release/podcasts-gtk",
        name="gnome-podcasts",
    )

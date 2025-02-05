pkgname = "gnome-podcasts"
pkgver = "0.7.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/podcasts"
source = f"{url}/-/archive/{pkgver}/podcasts-{pkgver}.tar.gz"
sha256 = "ecfc2354f014d0b49beed580312502661b909964655f24ebfd7e0e26d9f6b98d"
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

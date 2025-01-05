pkgname = "gnome-podcasts"
pkgver = "0.7.1"
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
    "openssl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "GTK-based podcast aggregator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/podcasts"
source = f"{url}/-/archive/{pkgver}/podcasts-{pkgver}.tar.gz"
sha256 = "933d33dfd0f36343f9c80f055a48e14307a0665b35097da176767ddbfe583399"
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

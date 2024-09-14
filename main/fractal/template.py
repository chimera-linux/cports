pkgname = "fractal"
pkgver = "8"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libshumate-devel",
    "openssl-devel",
    "pipewire-devel",
    "rust-std",
    "sqlite-devel",
    "xdg-desktop-portal-devel",
]
pkgdesc = "GTK Matrix client"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/fractal"
source = f"{url}/-/archive/{pkgver}/fractal-{pkgver}.tar.gz"
sha256 = "88c75438ffda8fd16bba5bdf3c1ffceedb8a707d0967b812421a107edb76af5f"
# check: has few actual tests, not worth a time-consuming cargo rebuild
# debug: quite massive, CARGO_PROFILE_RELEASE_DEBUG=line-tables-only in
# env makes it better but it's still ~260M
options = ["!check", "!debug"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/fractal")

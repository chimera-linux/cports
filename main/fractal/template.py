pkgname = "fractal"
pkgver = "9"
pkgrel = 1
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
    "libseccomp-devel",
    "libshumate-devel",
    "libwebp-devel",
    "openssl-devel",
    "pipewire-devel",
    "rust-std",
    "sqlite-devel",
    "xdg-desktop-portal-devel",
]
depends = ["glycin-loaders"]
pkgdesc = "GTK Matrix client"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/fractal"
source = f"{url}/-/archive/{pkgver}/fractal-{pkgver}.tar.gz"
sha256 = "61be5f378545fe4ef76feb7d5604aac6261a3dedcfb5dd756713eacc574d5373"
# check: has few actual tests, not worth a time-consuming cargo rebuild
# debug: quite massive, CARGO_PROFILE_RELEASE_DEBUG=line-tables-only in
# env makes it better but it's still ~260M
options = ["!check", "!debug"]


if self.profile().wordsize == 32:
    broken = "needs atomicu64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/fractal")

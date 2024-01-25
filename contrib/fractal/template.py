pkgname = "fractal"
pkgver = "6"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libshumate-devel",
    "pipewire-devel",
    "rust-std",
    "xdg-desktop-portal-devel",
]
pkgdesc = "GTK Matrix client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/fractal"
source = f"{url}/-/archive/{pkgver}/fractal-{pkgver}.tar.gz"
sha256 = "a730dffe5fd4859c16e0d84244a82f6ea843d4e464ee04e08fcb5bea61c248f2"
# no actual tests just formatting/etc
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self, wrksrc=".")
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_build(self):
    from cbuild.util import cargo

    # reduce 600MB debuginfo
    cargo.Cargo(self).build(
        env={"CARGO_PROFILE_RELEASE_DEBUG": "line-tables-only"}
    )


def post_install(self):
    self.install_bin(
        self.cwd / "target" / self.profile().triplet / "release" / "fractal"
    )

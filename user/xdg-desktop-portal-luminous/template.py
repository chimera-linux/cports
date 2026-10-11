pkgname = "xdg-desktop-portal-luminous"
pkgver = "0.1.21"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["cargo-auditable", "meson", "ninja", "pkgconf"]
makedepends = [
    "clang-libs",
    "glib-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "rust-std",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["xdg-desktop-portal"]
pkgdesc = "Xdg-desktop-portal for wlroots based compositors"
license = "GPL-3.0-or-later"
url = "https://github.com/waycrate/xdg-desktop-portal-luminous"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d6df0ac024409de9e38f0890799b0ef3eaf71156692cc48fc0fe9059f79e8b58"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    from cbuild.util import cargo

    self.install_lib(cargo.target_path(self, "xdg-desktop-portal-luminous"))
    self.install_bin(cargo.target_path(self, "lumious_headless_helper"))

    self.uninstall("usr/lib/systemd")

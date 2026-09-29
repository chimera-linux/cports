pkgname = "xdg-desktop-portal-umbriel"
pkgver = "0_git20260926"
pkgrel = 0
_commit = "d6bd72cabd83e3084fb2f2e24898d8ffa4a8c24f"
build_style = "meson"
configure_args = ["-Dpicker=enabled"]
hostmakedepends = ["glib-devel", "meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pipewire-devel",
    "sdbus-cpp-devel",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["xdg-desktop-portal", "xdg-desktop-portal-gtk"]
pkgdesc = "XDG desktop portal backend for Umbriel"
license = "MIT"
url = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "a7a19e75162577cf5ffeae37c14beb8d2020866cd84480d19d01b74aa53364ca"


def post_install(self):
    self.install_license("LICENSE")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)

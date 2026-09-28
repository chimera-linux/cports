pkgname = "wluma"
pkgver = "5.0.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "linux-headers",
    "pipewire-devel",
    "turnstile",
    "udev-devel",
    "v4l-utils-devel",
    "vulkan-loader-devel",
]
depends = ["iio-sensor-proxy"]
pkgdesc = "Automatic brightness adjustment based on screen contents and ALS"
license = "ISC"
url = "https://github.com/maximbaz/wluma"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1c6472f93f1995fe9e4d94fc878aed06b6ba0f111d5b86f13839f1d0c9d02372"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wluma.user")

pkgname = "wluma"
pkgver = "5.0.4"
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
sha256 = "e854621dce8522a1ad042093b08024526815ca94f79003e0a6186a8f98950e5c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wluma.user")

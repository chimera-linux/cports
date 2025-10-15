pkgname = "j4-dmenu-desktop"
pkgver = "3.2"
pkgrel = 2
build_style = "meson"
configure_args = ["-Denable-tests=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["catch2-devel", "fmt-devel", "spdlog-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Application launcher using dmenu"
license = "GPL-3.0-or-later"
url = "https://github.com/enkore/j4-dmenu-desktop"
source = f"{url}/archive/r{pkgver}.tar.gz"
sha256 = "99e2f394570f8fb0b1a2cde2926980fd9685ce60e1500b575057f8424c9ad555"

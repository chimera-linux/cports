pkgname = "alsa-ucm-conf-asahi"
pkgver = "7"
pkgrel = 0
archs = ["aarch64"]
depends = ["alsa-ucm-conf"]
pkgdesc = "Alsa UCM configuration for Asahi Linux"
license = "BSD-3-Clause"
url = "https://github.com/AsahiLinux/alsa-ucm-conf-asahi"
source = f"https://github.com/AsahiLinux/alsa-ucm-conf-asahi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9fe73275406f92c47b3433e12aff6db0774f8c18f79c5260d16e84e16cabd528"


def install(self):
    self.install_files("ucm2", "usr/share/alsa")
    self.install_license("LICENSE.asahi")

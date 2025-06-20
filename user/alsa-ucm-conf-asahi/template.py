pkgname = "alsa-ucm-conf-asahi"
pkgver = "8"
pkgrel = 0
archs = ["aarch64"]
depends = ["alsa-ucm-conf"]
pkgdesc = "Alsa UCM configuration for Asahi Linux"
license = "BSD-3-Clause"
url = "https://github.com/AsahiLinux/alsa-ucm-conf-asahi"
source = f"https://github.com/AsahiLinux/alsa-ucm-conf-asahi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e0a028ab4d6d5cf5033e293a4205071245911827be052e21a723ed6bd694efb1"


def install(self):
    self.install_files("ucm2", "usr/share/alsa")
    self.install_license("LICENSE.asahi")

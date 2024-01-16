pkgname = "chimera-artwork"
pkgver = "0.99.1"
pkgrel = 0
pkgdesc = "Chimera Linux artwork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-SA-4.0"
url = "https://chimera-linux.org"
source = f"https://github.com/chimera-linux/chimera-artwork/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "77b74b464d78938ebebd9f73f5dbf7a932aa43c0cdf11ed25358fb3fd49ce66c"


def do_install(self):
    for f in ["png", "svg"]:
        self.install_file(f"chimera-logo.{f}", "usr/share/chimera-artwork")
    for s in [16, 22, 32, 48, 64, 128, 256, 512, 1024]:
        self.install_file(
            f"icons/chimera-logo-{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name="chimera-logo.png",
        )
    self.install_file(
        "icons/chimera-logo.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    dp = "usr/share/backgrounds/chimera"
    self.install_file("chimera-bg-d.svg", dp, name="bg-d.svg")
    self.install_file("chimera-bg-l.svg", dp, name="bg-l.svg")
    self.install_file(
        self.files_path / "chimera.xml", "usr/share/gnome-background-properties"
    )

pkgname = "chimera-artwork"
pkgver = "0.1"
pkgrel = 0
pkgdesc = "Chimera Linux artwork"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC0-1.0"
url = "https://chimera-linux.org"

def do_install(self):
    for f in ["png", "svg"]:
        self.install_file(
            self.files_path / f"chimera-logo.{f}", "usr/share/chimera-artwork"
        )
    for s in [16, 22, 32, 48, 64, 128, 256, 512, 1024]:
        self.install_file(
            self.files_path / f"icons/chimera-logo-{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name = "chimera-logo.png"
        )
    self.install_file(
        self.files_path / "icons/chimera-logo.svg",
        "usr/share/icons/hicolor/scalable/apps"
    )

pkgname = "chimera-image-keys"
pkgver = "20231227"
pkgrel = 0
build_style = "meta"
depends = ["minisign"]
pkgdesc = "Chimera public keys for image verification"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


def do_install(self):
    for f in self.files_path.glob("*.pub"):
        self.install_file(f, "usr/share/chimera-image-keys")

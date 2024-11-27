pkgname = "steam-devices-udev"
pkgver = "1.0.0.61_git20230412"
pkgrel = 1
_commit = "13443480a64fe8f10676606bd57da6de89f8ccb1"
pkgdesc = "Udev rules for use with the Steam flatpak"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ValveSoftware/steam-devices"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "2e508acb093d1428f32c3f6b0bc836cc4a20ceef4afc92b6cdb7cf631400fd36"


def install(self):
    self.install_license("LICENSE")
    self.install_file("*.rules", "usr/lib/udev/rules.d", glob=True)

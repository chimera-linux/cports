pkgname = "asahi-scripts"
pkgver = "20250426.1"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
make_install_target = "install-chimera"
depends = ["asahi-fwextract"]
pkgdesc = "Asahi Linux maintenance scripts"
license = "MIT"
url = "https://github.com/AsahiLinux/asahi-scripts"
source = f"https://github.com/AsahiLinux/asahi-scripts/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8ccc68ced916acc0a21fc59077f6a0022aab2d3297385475243bde092d9d74ea"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/systemd")


@subpackage("asahi-udev")
def _(self):
    self.pkgdesc = "Asahi Linux udev rules"
    self.depends = ["udev-meta"]
    return ["usr/lib/udev"]

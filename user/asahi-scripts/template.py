pkgname = "asahi-scripts"
pkgver = "20250130"
pkgrel = 0
archs = ["aarch64"]
build_style = "makefile"
make_install_target = "install-chimera"
depends = ["asahi-fwextract"]
pkgdesc = "Asahi Linux maintenance scripts"
license = "MIT"
url = "https://github.com/AsahiLinux/asahi-scripts"
source = f"https://github.com/AsahiLinux/asahi-scripts/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a76c64bb971c45454454cdc0668a3f9401f1771c730e78da78bd022c74616c87"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/lib/systemd")


@subpackage("macsmc-battery-udev")
def _(self):
    self.pkgdesc = "Asahi Linux macsmc-battery udev rules"
    self.depends = ["udev-meta"]
    return ["usr/lib/udev"]

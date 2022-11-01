pkgname = "eudev"
pkgver = "3.2.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-hwdb", "--enable-manpages", "--disable-introspection"
]
hostmakedepends = ["pkgconf", "perl", "gperf"]
makedepends = ["libblkid-devel", "libkmod-devel", "linux-headers"]
checkdepends = ["xz", "perl"]
triggers = ["/usr/lib/udev/rules.d"]
pkgdesc = "Standalone implementation of systemd-udev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/eudev-project/eudev"
source = f"https://github.com/eudev-project/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "19847cafec67897da855fde56f9dc7d92e21c50e450aa79068a7e704ed44558b"
options = ["!splitudev"]

def post_install(self):
    # initramfs-tools
    self.install_file(
        self.files_path / "udev.hook",
        "usr/share/initramfs-tools/hooks",
        mode = 0o755, name = "udev"
    )
    self.install_file(
        self.files_path / "udev.init-top",
        "usr/share/initramfs-tools/scripts/init-top",
        mode = 0o755, name = "udev"
    )
    self.install_file(
        self.files_path / "udev.init-bottom",
        "usr/share/initramfs-tools/scripts/init-bottom",
        mode = 0o755, name = "udev"
    )
    # service
    self.install_file(
        self.files_path / "udevd.wrapper", "usr/libexec", mode = 0o755
    )
    self.install_service(self.files_path / "udevd", enable = True)

@subpackage("eudev-devel")
def _devel(self):
    return self.default_devel()

@subpackage("eudev-libs")
def _libs(self):
    return self.default_libs()

@subpackage("base-udev")
def _base(self):
    self.pkgdesc = "Base package for udev configs"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.build_style = "meta"

    return []

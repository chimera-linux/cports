pkgname = "eudev"
pkgver = "3.2.10"
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
url = "https://github.com/gentoo/eudev"
source = f"https://dev.gentoo.org/~blueness/eudev/eudev-{pkgver}.tar.gz"
sha256 = "87bb028d470fd1b85169349b44c55d5b733733dc2d50ddf1196e026725ead034"

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
    self.install_service(self.files_path / "udevd")

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

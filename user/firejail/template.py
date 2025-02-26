pkgname = "firejail"
pkgver = "0.9.72_git20250221"
pkgrel = 0
_commit = "733f9a9c487358ba73b06186ed348f086d8ac839"
build_style = "gnu_configure"
configure_args = ["--sysconfdir=/usr/share"]
configure_gen = []
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gawk", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Firejail SUID sandboxing tool"
maintainer = "hbog <herwig.bogaert@posteo.net>"
license = "GPL-2.0-only"
url = "https://github.com/netblue30/firejail"
source = f"{url}/archive/{_commit}.zip"
sha256 = "2a05497ac0dc2053b5e3aca2ddf5c32ab5176f60be102498bc849b3042225bb3"
file_modes = {"usr/bin/firejail": ("root", "root", 0o4755)}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

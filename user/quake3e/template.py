pkgname = "quake3e"
_commit = "f8372fd89f05a35c681f46b8dcfb08e14ad0857f"
pkgver = "1.32e_git20260820"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "USE_SYSTEM_JPEG=1",
    "USE_SYSTEM_OGG=1",
    "USE_SYSTEM_VORBIS=1",
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "curl-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libvorbis-devel",
    "libxxf86vm-devel",
    "sdl2-compat-devel",
    "vulkan-headers",
]
pkgdesc = "Improved Quake III Arena engine"
license = "GPL-2.0-only"
url = "https://github.com/ec-/quake3e"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "6edf70c1a6b7a692bf053405fc716315c02305527f01bcc7e8bfaaa6ed00bc93"
# no tests defined
options = ["!check"]


def install(self):
    self.do(
        "make",
        *make_build_args,
        f"DESTDIR={self.chroot_destdir}/usr/lib/quake3e",
        "install",
    )
    self.install_bin(self.files_path / "quake3e")
    self.install_file("docs/quake3e*", "usr/share/doc/quake3e", glob=True)

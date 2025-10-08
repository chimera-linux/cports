pkgname = "feh"
pkgver = "3.11.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "exif=1",
    "help=1",
    "inotify=1",
    "magic=1",
]
make_check_target = "test"
make_use_env = True
makedepends = [
    "curl-devel",
    "file-devel",
    "imlib2-devel",
    "libexif-devel",
    "libpng-devel",
    "libx11-devel",
    "libxinerama-devel",
    "libxt-devel",
]
checkdepends = ["perl", "perl-test-command", "mandoc"]
pkgdesc = "Fast and light image viewer"
license = "MIT"
url = "https://feh.finalrewind.org"
source = f"{url}/feh-{pkgver}.tar.bz2"
sha256 = "020f8bce84c709333dcc6ec5fff36313782e0b50662754947c6585d922a7a7b2"


def post_install(self):
    self.install_license("COPYING")

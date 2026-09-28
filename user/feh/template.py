pkgname = "feh"
pkgver = "3.12.2"
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
sha256 = "7ce358b18a7f37bcc97a09b4efd89fdadd54cd8e7032db345f61e66dd04b1c3f"


def post_install(self):
    self.install_license("COPYING")

pkgname = "v4l-utils"
pkgver = "1.30.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dqv4l2=disabled", "-Dudevdir=/usr/lib/udev"]
hostmakedepends = [
    "bash",
    "gettext-devel",
    "gsed",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "glu-devel",
    "json-c-devel",
    "libbpf-devel",
    "libjpeg-turbo-devel",
    "libx11-devel",
    "mesa-devel",
    "udev-devel",
]
pkgdesc = "Userspace tools and libraries for V4L"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://linuxtv.org/wiki/index.php/V4l-utils"
source = f"https://linuxtv.org/downloads/v4l-utils/v4l-utils-{pkgver}.tar.xz"
sha256 = "c1cf549c2ec3cf39eb5ec7bf15731349e61b26a21b5e963922db422333bae197"
tool_flags = {
    # mmap64, open64
    "CXXFLAGS": ["-D_LARGEFILE64_SOURCE"],
    "LDFLAGS": ["-largp"],
}


@subpackage("v4l-utils-devel")
def _(self):
    return self.default_devel()

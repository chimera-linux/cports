pkgname = "crun"
pkgver = "1.30.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
hostmakedepends = [
    "autoconf",
    "automake",
    "go-md2man",
    "pkgconf",
    "python",
    "slibtool",
]
makedepends = [
    "argp-standalone",
    "blake3-devel",
    "json-c-devel",
    "libcap-devel",
    "libseccomp-devel",
]
pkgdesc = "Fast and lightweight OCI runtime"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.zst"
sha256 = "d62b89a82520a553edf63fd3ae11275be6f16ec86ed90d8ef7b113d06b239fa2"
hardening = ["vis", "cfi"]


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.uninstall("usr/lib/libcrun.a")

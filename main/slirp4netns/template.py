pkgname = "slirp4netns"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libcap-devel",
    "libseccomp-devel",
    "libslirp-devel",
]
pkgdesc = "User-mode networking for unprivileged network namespaces"
license = "GPL-2.0-or-later"
url = "https://github.com/rootless-containers/slirp4netns"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c98ef2679c7b8c96eed95409138a22904a0550494d191385637e953534d15c75"
# cfi failure likely due to libslirp non-cfi timer shenanigans
hardening = ["vis", "!cfi"]
# needs ncat from nmap
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="slirp4netns.conf",
    )

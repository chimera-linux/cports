pkgname = "slirp4netns"
pkgver = "1.3.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/rootless-containers/slirp4netns"
source = f"https://github.com/rootless-containers/slirp4netns/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "551a63647114a0c50dd115640161c9330832e2466f602fd3d1eaf95d3226baab"
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

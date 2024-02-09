pkgname = "slirp4netns"
pkgver = "1.2.3"
pkgrel = 1
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
sha256 = "acce648fab8fe5f113c41a8fd6d20177708519b4ddaa60f845e1998a17b22ca5"
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

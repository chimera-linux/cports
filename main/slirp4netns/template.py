pkgname = "slirp4netns"
pkgver = "1.3.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/rootless-containers/slirp4netns"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a3b7c7b593b279c46d25a48b583371ab762968e98b6a46457d8d52a755852eb9"
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

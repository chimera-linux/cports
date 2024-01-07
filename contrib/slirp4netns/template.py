pkgname = "slirp4netns"
pkgver = "1.2.2"
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
sha256 = "2450afb5730ee86a70f9c3f0d3fbc8981ab8e147246f4e0d354f0226a3a40b36"
hardening = ["vis", "cfi"]
# needs ncat from nmap
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="slirp4netns.conf",
    )

pkgname = "slirp4netns"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake"]
makedepends = [
    "libseccomp-devel",
    "libcap-devel",
    "glib-devel",
    "libslirp-devel",
]
depends = ["libseccomp", "libcap", "libslirp"]
checkdepends = ["bash", "util-linux-ns", "mount", "iproute2", "jq"]
pkgdesc = "User-mode networking for unprivileged network namespaces"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "GPL-2.0-only"
url = "https://github.com/rootless-containers/slirp4netns"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "51aa240e1e29905ed35b449ca718539a01221aab3b6d291c4dc6777f0eb9d7d9"
# checkdepends missing: ncat, uses "sleep infinity"
options = ["!check"]

pkgname = "bubblewrap"
pkgver = "0.12.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dassume_kernel=6.18.0"]
hostmakedepends = [
    "bash-completion",
    "docbook-xsl-nons",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs", "util-linux-mount"]
pkgdesc = "Unprivileged sandboxing tool"
license = "LGPL-2.1-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"{url}/releases/download/v{pkgver}/bubblewrap-{pkgver}.tar.xz"
sha256 = "9760d007363e3abba7c747489910f9f82d9fca53ba3bd3282e396fa3c97a3314"
hardening = ["vis", "cfi"]

# efault instead of econnrefused for various assertions
if self.profile().arch not in ["aarch64", "loongarch64", "riscv64"]:
    checkdepends += ["python-libseccomp"]

pkgname = "bubblewrap"
pkgver = "0.13.1"
pkgrel = 0
build_style = "meson"
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
sha256 = "0e85c8702248b8dd64144f594147553650cdd0e4c951690345faace79c217c4d"
hardening = ["vis", "cfi"]

# efault instead of econnrefused for various assertions
if self.profile.arch not in ["aarch64", "loongarch64", "riscv64"]:
    checkdepends += ["python-libseccomp"]

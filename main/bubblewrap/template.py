pkgname = "bubblewrap"
pkgver = "0.13.0"
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
sha256 = "4734237473c0e5d695e4e9034a34e43b2dbf5164655bd13fa59ae376b2b7a765"
hardening = ["vis", "cfi"]

# efault instead of econnrefused for various assertions
if self.profile.arch not in ["aarch64", "loongarch64", "riscv64"]:
    checkdepends += ["python-libseccomp"]

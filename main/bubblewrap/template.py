pkgname = "bubblewrap"
pkgver = "0.11.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "libxslt-progs", "docbook-xsl-nons"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs", "util-linux-mount"]
pkgdesc = "Unprivileged sandboxing tool"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"{url}/releases/download/v{pkgver}/bubblewrap-{pkgver}.tar.xz"
sha256 = "c1b7455a1283b1295879a46d5f001dfd088c0bb0f238abb5e128b3583a246f71"
hardening = ["vis", "cfi"]

# efault instead of econnrefused for various assertions
if self.profile().arch not in ["aarch64", "loongarch64", "riscv64"]:
    checkdepends += ["python-libseccomp"]

pkgname = "bubblewrap"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "libxslt-progs", "docbook-xsl-nons"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs", "util-linux-mount"]
pkgdesc = "Unprivileged sandboxing tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"{url}/releases/download/v{pkgver}/bubblewrap-{pkgver}.tar.xz"
sha256 = "988fd6b232dafa04b8b8198723efeaccdb3c6aa9c1c7936219d5791a8b7a8646"
hardening = ["vis", "cfi"]

# seccomp tests fail on aarch64 with efault instead of econnrefused for various assertions
if self.profile().arch != "aarch64":
    checkdepends += ["python-libseccomp"]

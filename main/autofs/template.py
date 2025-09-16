pkgname = "autofs"
pkgver = "5.1.9"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-libtirpc",
    "--with-mapdir=/etc/autofs",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "heimdal-devel",
    "libsasl-devel",
    "libtirpc-devel",
    "libxml2-devel",
    "openldap-devel",
    "openssl3-devel",
]
pkgdesc = "Kernel-based automounter"
license = "GPL-2.0-or-later"
url = "https://www.kernel.org/pub/linux/daemons/autofs"
source = f"{url}/v{pkgver.split('.')[0]}/autofs-{pkgver}.tar.xz"
sha256 = "87e6af6a03794b9462ea519781e50e7d23b5f7c92cd59e1142c85d2493b3c24b"
# check: no tests
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "automount")

    # install sample configuration
    self.install_file(
        "samples/autofs.conf.default", "etc/autofs", name="autofs.conf"
    )
    self.install_file("samples/auto.master", "etc/autofs")
    self.install_file("samples/auto.misc", "etc/autofs")
    self.install_file("samples/auto.net", "etc/autofs", mode=0o755)
    self.install_file("samples/auto.smb", "etc/autofs", mode=0o755)
    self.install_file("samples/autofs.init.conf", "etc/default", name="autofs")

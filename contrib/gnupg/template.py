pkgname = "gnupg"
pkgver = "2.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-all-tests"]
make_check_env = {
   "TESTFLAGS": f"--parallel={self.conf_jobs}"
}
hostmakedepends = ["pkgconf"]
makedepends = ["libbz2-devel", "libassuan-devel", "libksba-devel", "npth-devel", "libgpg-error-devel", "libgcrypt-devel", "gnutls-devel", "libusb-devel", "sqlite-devel", "readline-devel"]
depends = ["pinentry"]
pkgdesc = "GNU Privacy Guard (2.x)"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "1d79158dd01d992431dd2e3facb89fdac97127f89784ea2cb610c600fb0c1483"

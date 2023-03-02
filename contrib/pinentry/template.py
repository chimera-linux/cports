pkgname = "pinentry"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args= ["--enable-pinentry-tty", "--enable-pinentry-curses", "--enable-pinentry-gnome3", "--enable-fallback-curses", "--enable-libsecret"]
make_install_env = {
  "PINENTRY_DEFAULT": "pinentry-curses"
}
hostmakedepends = ["pkgconf"]
makedepends= ["ncurses-devel", "libassuan-devel", "libgpg-error-devel", "gcr-devel", "libsecret-devel"]
pkgdesc = "PIN or passphrase entry dialogs for GnuPG"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "457a185e5a85238fb945a955dc6352ab962dc8b48720b62fc9fa48c7540a4067"

def post_install(self):
   # pinentry tries to default to gnome3, which is not desired
   # so wipe the symlink and use curses instead
   self.rm(self.destdir / "usr/bin/pinentry")
   self.install_link("pinentry-curses", "usr/bin/pinentry")

@subpackage("pinentry-tty")
def _tty(self):
   return ["usr/bin/pinentry-tty"]

@subpackage("pinentry-gnome3")
def _gnome3(self):
   return ["usr/bin/pinentry-gnome3"]

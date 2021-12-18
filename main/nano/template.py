pkgname = "nano"
pkgver = "5.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"https://www.nano-editor.org/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "757db8cda4bb2873599e47783af463e3b547a627b0cabb30ea7bf71fb4c24937"

def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")

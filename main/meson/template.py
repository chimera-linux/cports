pkgname = "meson"
pkgver = "0.61.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel", "python-setuptools"]
depends = ["ninja", "python-setuptools"]
pkgdesc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://mesonbuild.com"
source = f"https://github.com/mesonbuild/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9c884434469471f3fe0cbbceb9b9ea0c8047f19e792940e1df6595741aae251b"
# meson is early in our bootstrap path but has a million checkdepends
options = ["!check"]

def post_install(self):
    # vim syntax
    self.install_dir("usr/share/vim/vimfiles")
    for f in ["ftdetect", "ftplugin", "indent", "syntax"]:
        self.install_files(
            f"data/syntax-highlighting/vim/{f}", "usr/share/vim/vimfiles"
        )
    with self.pushd("data/shell-completions"):
        # bashcomp
        self.install_file("bash/meson", "usr/share/bash-completion/completions")
        # zshcomp
        self.install_file("zsh/_meson", "usr/share/zsh/site-functions")

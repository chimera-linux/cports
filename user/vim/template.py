pkgname = "vim"
pkgver = "9.1.0377"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl",
    "--enable-gui=no",
    # makes them dynamically loaded so we don't install every scripting language
    # by default
    "--enable-luainterp=dynamic",
    "--enable-rubyinterp=dynamic",
    "--enable-python3interp=dynamic",
    "--with-compiledby=Chimera Linux",
    "--without-x",
]
# completely broken reconf for some reason
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake"]
makedepends = [
    "acl-devel",
    "libsodium-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "ruby-devel",
    "python-devel",
]
depends = [f"xxd={pkgver}-r{pkgrel}"]
pkgdesc = "Vi-style text editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "Vim"
url = "https://vim.org"
source = f"https://github.com/vim/vim/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c9f1073bad73187fec6fa5be1ddf304c4d9dc086e54abca640895c85a01b7231"
# FIXME cfi int
hardening = ["vis", "!cfi", "!int"]
# TODO
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "vimrc", "etc")
    self.install_license("LICENSE")
    # chimerautils-extra ex/view conflict with these symlinks
    # TODO: just rename and update the code in main.c:parse_command_name
    self.rm(self.destdir / "usr/bin/ex")
    self.rm(self.destdir / "usr/share/man/*/man1/ex.1", glob=True)
    self.rm(self.destdir / "usr/bin/view")
    self.rm(self.destdir / "usr/share/man/*/man1/view.1", glob=True)


@subpackage("xxd")
def _xxd(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

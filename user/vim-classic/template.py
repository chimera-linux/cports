pkgname = "vim-classic"
pkgver = "8.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl",
    "--enable-gui=no",
    # dynamically loaded so the language runtimes don't need to be installed
    "--enable-luainterp=dynamic",
    "--enable-rubyinterp=dynamic",
    "--enable-python3interp=dynamic",
    "--with-compiledby=Chimera Linux",
    "--without-x",
]
configure_gen = ["autoreconf", "-if", "src"]
make_dir = "."
# install targets race each other for directories
make_install_args = ["-j1"]
make_check_target = "test"
hostmakedepends = ["automake"]
_luaver = "5.4"
makedepends = [
    "acl-devel",
    "libsodium-devel",
    f"lua{_luaver}-devel",
    "ncurses-devel",
    "python-devel",
    "ruby-devel",
]
depends = [self.with_pkgver("vim-classic-xxd")]
provides = ["vim=8.2.0148"]
pkgdesc = "Vim Classic is a fork of Vim 8.x for long-term maintenance"
license = "Vim"
url = "https://www.vim-classic.org"
source = f"https://git.sr.ht/~sircmpwn/vim-classic/archive/v{pkgver}.tar.gz"
sha256 = "1d9baef8dab6751145b7c4460e85c0af1f4c432bf8ff03d8db13b977fca31e8c"
tool_flags = {
    "CFLAGS": [
        '-DSYS_VIMRC_FILE="/usr/share/vim/vimrc"',
        f'-DDYNAMIC_LUA_DLL="liblua{_luaver}.so.{_luaver}"',
    ]
}
# require a million system-specific fixes
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "vimrc", "usr/share/vim")
    self.install_license("LICENSE")
    # gui is not built, refers to nothing
    self.uninstall("usr/share/applications/gvim.desktop")
    # chimerautils-extra ex/view conflict with these symlinks
    self.uninstall("cmd:ex")
    self.uninstall("cmd:view")


@split("xxd")
def _(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    self.provides = [self.with_pkgver("xxd")]
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

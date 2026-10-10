pkgname = "vim-classic"
pkgver = "8.3.0"
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
makedepends = [
    "acl-devel",
    "libsodium-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "python-devel",
    "ruby-devel",
]
depends = [self.with_pkgver("vim-classic-xxd")]
pkgdesc = "Vim Classic is a fork of Vim 8.x for long-term maintenance"
license = "Vim"
url = "https://www.vim-classic.org"
source = f"https://git.sr.ht/~sircmpwn/vim-classic/archive/v{pkgver}.tar.gz"
sha256 = "6e1c97c8269e9354bbc474f0efa7e1e0b23fcdb6075067474d731a9bfac6e8ef"
tool_flags = {"CFLAGS": ['-DSYS_VIMRC_FILE="/usr/share/vim/vimrc"']}
# require a million system-specific fixes
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "vimrc", "usr/share/vim")
    self.install_license("LICENSE")
    # gui is not built, refers to nothing
    self.uninstall("usr/share/applications/gvim.desktop")
    # chimerautils-extra ex/view conflict with these symlinks
    # TODO: just rename and update the code in main.c:parse_command_name
    self.uninstall("usr/bin/ex")
    self.uninstall("usr/share/man/*/man1/ex.1", glob=True)
    self.uninstall("usr/bin/view")
    self.uninstall("usr/share/man/*/man1/view.1", glob=True)


@subpackage("vim-classic-xxd")
def _(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    self.provides = [self.with_pkgver("xxd")]
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

# the vimrc is shared with vim-classic, rebuild that too if you change it
pkgname = "vim"
pkgver = "9.2.1172"
pkgrel = 1
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
depends = [self.with_pkgver("vim-xxd")]
pkgdesc = "Vi-style text editor"
license = "Vim"
url = "https://www.vim.org"
source = f"https://github.com/vim/vim/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d4f7a793d2cf80ad6bb09085746515979d049e79e5839d8b68325688b47af297"
tool_flags = {"CFLAGS": ['-DSYS_VIMRC_FILE="/usr/share/vim/vimrc"']}
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


@subpackage("vim-xxd")
def _(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    self.provides = [self.with_pkgver("xxd")]
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

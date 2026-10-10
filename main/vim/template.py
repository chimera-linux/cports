pkgname = "vim"
pkgver = "9.1.0880"
pkgrel = 4
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
sha256 = "011d2653dffbd74239794348fdd01d67fcdaddb55c27f7b706f4cc00a3b16f22"
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


@subpackage("vim-xxd")
def _(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    self.provides = [self.with_pkgver("xxd")]
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

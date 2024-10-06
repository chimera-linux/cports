pkgname = "vim"
pkgver = "9.1.0764"
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
make_dir = "."
make_check_target = "test"
makedepends = [
    "acl-devel",
    "libsodium-devel",
    "lua5.4-devel",
    "ncurses-devel",
    "python-devel",
    "ruby-devel",
]
depends = [self.with_pkgver("xxd")]
pkgdesc = "Vi-style text editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "Vim"
url = "https://www.vim.org"
source = f"https://github.com/vim/vim/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "874be6146792d67ae47dc8d89f9d32558a266df87a81f5f80ad1b9b4cb31c1a1"
tool_flags = {"CFLAGS": ['-DSYS_VIMRC_FILE="/etc/vim/vimrc"']}
hardening = ["vis", "!cfi"]
# require a million system-specific fixes
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "vimrc", "etc/vim")
    self.install_license("LICENSE")
    # chimerautils-extra ex/view conflict with these symlinks
    # TODO: just rename and update the code in main.c:parse_command_name
    self.uninstall("usr/bin/ex")
    self.uninstall("usr/share/man/*/man1/ex.1", glob=True)
    self.uninstall("usr/bin/view")
    self.uninstall("usr/share/man/*/man1/view.1", glob=True)


@subpackage("xxd")
def _(self):
    self.pkgdesc = "Tool for viewing/editing hex dumps"
    return [
        "usr/bin/xxd",
        "usr/share/man/man1/xxd.1",
        "usr/share/man/*/man1/xxd.1",
    ]

pkgname = "zsh"
pkgver = "5.9"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--disable-gdbm",
    "--enable-etcdir=/etc/zsh",
    "--enable-zshenv=/etc/zsh/zshenv",
    "--enable-zlogin=/etc/zsh/zlogin",
    "--enable-zlogout=/etc/zsh/zlogout",
    "--enable-zprofile=/etc/zsh/zprofile",
    "--enable-zshrc=/etc/zsh/zshrc",
    "--enable-maildir-support",
    "--enable-function-subdirs",
    "--enable-fndir=/usr/share/zsh/functions",
    "--enable-scriptdir=/usr/share/zsh/scripts",
    "--enable-multibyte",
    "--enable-pcre",
    "--enable-cap",
    "--with-term-lib=ncursesw",
    "--with-tcsetpgrp",
    "zsh_cv_shared_environ=yes",
    "zsh_cv_sys_dynamic_execsyms=yes",
    "zsh_cv_func_dlsym_needs_underscore=no",
]
make_dir = "."  # bad build system
# https://www.zsh.org/mla/workers/2021/msg00805.html
make_check_wrapper = ["env", "-u", "LC_COLLATE", "-u", "LANG"]
hostmakedepends = ["pkgconf", "texinfo", "automake"]
makedepends = ["ncurses-devel", "pcre2-devel", "libcap-devel"]
pkgdesc = "Z shell"
license = "MIT AND GPL-3.0-or-later"
url = "https://www.zsh.org"
source = f"{url}/pub/zsh-{pkgver}.tar.xz"
sha256 = "9b8d1ecedd5b5e81fbf1918e876752a7dd948e05c1a0dba10ab863842d45acd5"
# FIXME int: test failures
hardening = ["!int"]


def post_patch(self):
    self.rm("Completion/Linux/Command/_pkgtool")

    for f in [
        "AIX",
        "BSD",
        "Cygwin",
        "Darwin",
        "Debian",
        "Mandriva",
        "openSUSE",
        "Redhat",
        "Solaris",
    ]:
        self.rm(f"Completion/{f}", recursive=True)

    # remove failing tests
    self.rm("Test/D07multibyte.ztst")
    self.rm("Test/V09datetime.ztst")
    self.rm("Test/Y03arguments.ztst")


def post_install(self):
    self.install_license("LICENCE")
    self.install_shell("/usr/bin/zsh")
    self.install_file(self.files_path / "zprofile", "etc/zsh")
    # hardlink
    self.uninstall("usr/bin/zsh")
    self.install_link("usr/bin/zsh", f"zsh-{pkgver}")

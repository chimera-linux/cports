pkgname = "chroot-bash"
version = "5.1.004"
revision = 1
_bash_distver = version[0:version.rfind(".")]
_bash_patchlevel = int(version[len(_bash_distver) + 1:])
_patchprefix = "bash" + _bash_distver.replace(".", "")
wrksrc = f"bash-{_bash_distver}"
build_style = "gnu_configure"
# need 'bash_cv_termcap_lib=gnutermcap' in order to force bash to use the
# bundled termcap library when bootstrapping from source on a foreign system
configure_args = [
    "--without-bash-malloc", "--without-curses",
    "--without-installed-readline", "--disable-nls",
    "bash_cv_termcap_lib=gnutermcap"
]
short_desc="GNU Bourne Again Shell -- for xbps-src use"
maintainer="Enno Boland <gottox@voidlinux.org>"
license="GPL-3.0-or-later"
homepage="http://www.gnu.org/software/bash/bash.html"

from cbuild import sites

distfiles = [f"{sites.gnu}/bash/bash-{_bash_distver}.tar.gz"]
skip_extraction = []

_url = f"{sites.gnu}/bash/bash-{_bash_distver}-patches"

for p in range(1, _bash_patchlevel + 1):
    p = "00" + str(p)
    distfiles.append(f"{_url}/{_patchprefix}-{p}")
    skip_extraction.append(f"{_patchprefix}-{p}")

checksum = [
    "cc012bc860406dcf42f64431bcd3d2fa7560c02915a601aba9cd597a39329baa",
    "ebb07b3dbadd98598f078125d0ae0d699295978a5cdaef6282fe19adef45b5fa",
    "15ea6121a801e48e658ceee712ea9b88d4ded022046a6147550790caf04f5dbe",
    "22f2cc262f056b22966281babf4b0a2f84cb7dd2223422e5dcd013c3dcbab6b1",
    "9aaeb65664ef0d28c0067e47ba5652b518298b3b92d33327d84b98b28d873c86",
]

bootstrap = True
provides = [f"bash-{version}_{revision}"]
conflicts = [
    "bash>=0", "dash>=0", "busybox>=0", "loksh>=0",
    "mksh>=0", "oksh>=0", "yash>=0"
]

def post_patch(self):
    for p in range(1, _bash_patchlevel + 1):
        p = "00" + str(p)
        self.log(f" Applying patch {_patchprefix}-{p}.")
        self.do("patch", [
            "-sNp0", "-i",
            str(self.chroot_hostdir / "sources" \
                / f"chroot-bash-{version}/{_patchprefix}-{p}")
        ])

def post_install(self):
    self.install_link("bash", "usr/bin/sh")
    self.rmtree("usr/lib")
    self.rmtree("usr/share")
    self.rmtree("usr/include")

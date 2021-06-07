pkgname = "xbps-triggers"
version = "0.120"
revision = 1
bootstrap = True
short_desc = "XBPS triggers for Void Linux"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "Public Domain"
homepage = "https://voidlinux.org"

def do_install(self):
    tdir = "usr/libexec/" + pkgname

    self.install_dir(tdir)

    for f in self.files_path.iterdir():
        tger = f.name
        self.install_file(f, tdir, mode = 0o754)
        with open(self.destdir / tdir / tger, "a") as f:
            f.write("# end\n")

    self.install_dir("var/db/xbps")
    self.install_link("../../../" + tdir, "var/db/xbps/triggers")
